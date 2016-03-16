#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports
import concurrent.futures
import ipaddress

from nmb.NetBIOS import NetBIOS
# Core Django imports
from django.db.utils import IntegrityError
from django.utils import timezone
from django.db import transaction
# Third-party app imports

# Imports from your apps
from .ping import quiet_ping
from .models import Host


# enqueue(populate_trends, args=(self,), kwargs={'x': 1,}, timeout=500)

def init_subnet(subnet):
    _interface = ipaddress.ip_interface(subnet.subnet_address + "/" + subnet.mask)
    _networks = _interface.network

    subnet.mask = str(_networks.netmask)
    subnet.subnet_address = str(_networks.network_address)
    try:
        subnet.save()
    except IntegrityError:
        subnet.delete()
        return

    _host_ip_str_list = []
    for _host_ip in list(_networks.hosts()):
        _host_ip_str_list.append(str(_host_ip))

    for exist_host in subnet.hosts.all():
        if str(exist_host.ip_address) in _host_ip_str_list:
            if not exist_host.mask == subnet.mask:
                exist_host.mask = subnet.mask
                exist_host.save()
            _host_ip_str_list.remove(str(exist_host.ip_address))
        else:
            exist_host.delete()
    need_create_host = []
    for _host_ip_str in _host_ip_str_list:
        host = Host(ip_address=_host_ip_str, mask=subnet.mask, subnet=subnet)
        need_create_host.append(host)

    Host.objects.bulk_create(need_create_host)
    subnet.been_init = True
    subnet.save()
    return subnet


def scan_host(host, ping_timeout=500, ping_packet=3, smb_timeout=2, save=True):
    maxTime, minTime, avrgTime, fracLoss = quiet_ping(hostname=host.ip_address, timeout=ping_timeout, count=ping_packet, path_finder=True)
    if ping_packet > 3:
        fracLoss_cap = 0.3
    else:
        fracLoss_cap = 0
    if fracLoss <= fracLoss_cap:
        host.ping_last_success_time = timezone.datetime.now()
        host.ping_last_success_delay = maxTime
    n = NetBIOS()
    try:
        host.hostname = n.queryIPForName(host.ip_address, timeout=smb_timeout)[0]
    except:
        pass
    n.close()
    host.latest_scan_time = timezone.datetime.now()
    if save:
        host.save()
    return host


def scan_subnet(subnet, ping_timeout=3000, ping_packet=5, smb_timeout=2, max_workers=None):
    host_list = list(subnet.hosts.all())
    scaned_host_list = []
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=max_workers)

    futures = [executor.submit(scan_host, host, ping_timeout=ping_timeout, ping_packet=ping_packet, smb_timeout=smb_timeout, save=False) for host in host_list]

    for future in concurrent.futures.as_completed(futures, timeout=120):
        scaned_host_list.append(future.result())
    executor.shutdown()

    # print(scaned_host_list)

    with transaction.atomic():
        # This code executes inside a transaction.
        for host in scaned_host_list:
            host.save()
        subnet.latest_scan_time = timezone.datetime.now()
        subnet.save()
    return subnet
