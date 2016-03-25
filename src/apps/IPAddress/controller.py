#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports
import sys
import re
import concurrent.futures
import ipaddress
import subprocess
import pprint

from nmb.NetBIOS import NetBIOS
# Core Django imports
from django.db.utils import IntegrityError
from django.utils import timezone
from django.db import transaction
from django.utils.translation import ugettext_lazy as _
# Third-party app imports

# Imports from your apps
from .models import Host


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


def ping_host(host, count=1, timeout=1, save=True):
    if sys.platform == "win32":
        p = subprocess.Popen(['ping', '-n', str(1), '-w', str(timeout * 1000), host.ip_address], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    else:
        p = subprocess.Popen(['/bin/ping', '-c', str(count), '-W', str(timeout), host.ip_address], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate(timeout=count * (timeout + 5))
    host.ping_stdout = str(out)
    host.ping_latest_time = timezone.datetime.now()
    if p.returncode == 0:
        host.ping_last_success_time = host.ping_latest_time
    if save:
        host.save()
    return host


def ping_subnet(subnet):
    if sys.platform == "win32":
        # no fping in windows =.=!
        return subnet
    else:
        p = subprocess.Popen(['/usr/bin/fping', '-g', subnet.cidr(), '-c1', '-q'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = p.communicate(timeout=120)

    fping_regex = re.compile('(?P<ip_address>^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(?P<xmt>\d{1,2})\/(?P<rcv>\d{1,2})\/(?P<loss>\d{1,3})%.*', re.DOTALL)
    fping_result = {}

    for line in error.decode().splitlines():
        try:
            fping_result[fping_regex.search(line).groupdict()["ip_address"]] = int(fping_regex.search(line).groupdict()["loss"])
        except:
            pass

    pprint.pprint(fping_result)
    with transaction.atomic():
        for host in subnet.hosts.all():
            host.ping_latest_time = timezone.datetime.now()
            if fping_result.get(host.ip_address, 1) == 0:
                host.ping_last_success_time = timezone.datetime.now()
            host.save()
        subnet.ping_latest_time = timezone.datetime.now()
        subnet.save()

    return subnet


def reverse_host(host, timeout=1, save=True):
    n = NetBIOS()
    try:
        host.hostname = n.queryIPForName(host.ip_address, timeout=timeout)[0]
    except:
        pass
    n.close()
    host.reverse_latest_time = timezone.datetime.now()
    if save:
        host.save()
    return host


def reverse_subnet(subnet):
    host_list = list(subnet.hosts.all())
    scaned_host_list = []
    executor = concurrent.futures.ThreadPoolExecutor()
    futures = [executor.submit(reverse_host, host, save=False) for host in host_list]
    for future in concurrent.futures.as_completed(futures, timeout=120):
        scaned_host_list.append(future.result())
    executor.shutdown()

    with transaction.atomic():
        for host in scaned_host_list:
            host.save()
        subnet.reverse_latest_time = timezone.datetime.now()
        subnet.save()
    return subnet


def ip_to_local(ip_address):
    if ip_address is None:
        return _("无")
    try:
        host = Host.objects.get(ip_address=ip_address)
    except Host.DoesNotExist:
        return _("IP无归属子网")
    if host.subnet.department is None:
        return host.subnet.summary
    else:
        return host.subnet.department.title


def ip_to_department(ip_address):
    if ip_address is None:
        return None
    try:
        host = Host.objects.get(ip_address=ip_address)
    except Host.DoesNotExist:
        return None
    if host.subnet.department is None:
        return None
    else:
        return host.subnet.department
