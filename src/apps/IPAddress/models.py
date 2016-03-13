#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

# Create your models here.

# Stdlib imports
import ipaddress
from nmb.NetBIOS import NetBIOS
import django_rq

# Core Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.utils import IntegrityError
from django.utils import timezone

# Third-party app imports


# Imports from your apps
from apps.Core.models import CommonModel
from apps.BranchManager.models import Department

from .ping import quiet_ping


class Subnet(CommonModel):
    subnet_address = models.GenericIPAddressField(verbose_name=_("子网地址"))
    mask = models.GenericIPAddressField(verbose_name=_("子网掩码"), default="255.255.255.0")

    gateway = models.GenericIPAddressField(verbose_name=_("网关"), null=True, blank=True)
    vlan = models.IntegerField(verbose_name=_("VLAN ID"), default=1)

    department = models.ForeignKey(to=Department, verbose_name=_("部门"), related_name="subnet", null=True, blank=True)

    summary = models.CharField(max_length=128, verbose_name=_("简介"), default="None")
    description = models.TextField(max_length=255, blank=True, verbose_name=_("详细描述"), default="None")

    been_init = models.BooleanField(default=False, editable=False)

    def _init_hosts(self):
        _interface = ipaddress.ip_interface(self.subnet_address + "/" + self.mask)
        _networks = _interface.network

        self.mask = str(_networks.netmask)
        self.subnet_address = str(_networks.network_address)
        try:
            self.save()
        except IntegrityError:
            self.delete()
            return

        _host_ip_str_list = []
        for _host_ip in list(_networks.hosts()):
            _host_ip_str_list.append(str(_host_ip))

        for exist_host in self.hosts.all():
            if str(exist_host.ip_address) in _host_ip_str_list:
                if not exist_host.mask == self.mask:
                    exist_host.mask = self.mask
                    exist_host.save()
                _host_ip_str_list.remove(str(exist_host.ip_address))
            else:
                exist_host.delete()
        need_create_host = []
        for _host_ip_str in _host_ip_str_list:
            host = Host(ip_address=_host_ip_str, mask=self.mask, subnet=self)
            need_create_host.append(host)

        Host.objects.bulk_create(need_create_host)
        self.been_init = True
        self.save()

    def cidr(self):
        return str(ipaddress.ip_interface(self.subnet_address + "/" + self.mask).network)

    def get_locale(self):
        if self.department is None:
            return self.summary
        return self.department.title

    def __unicode__(self):
        return self.cidr()
        # return self.summary

    class Meta:
        unique_together = ('subnet_address', 'mask')
        verbose_name = _("子网")
        verbose_name_plural = verbose_name


class Host(CommonModel):
    ip_address = models.GenericIPAddressField(verbose_name=_("子网地址"))
    mask = models.GenericIPAddressField(verbose_name=_("子网掩码"), default="255.255.255.0")
    subnet = models.ForeignKey(to=Subnet, verbose_name=_("子网"), related_name="hosts")
    description = models.TextField(max_length=255, default="None", verbose_name=_("详细描述"))

    latest_scan_time = models.DateTimeField(default=timezone.datetime.now, verbose_name=_("最后扫描时间"))

    # Reverse lookup
    hostname = models.CharField(max_length=255, verbose_name=_("主机名"), null=True, blank=True, default=None)
    # hostname_latest_time = models.DateTimeField(default=timezone.datetime.now)

    # 最近一次ping
    # ping_latest_time = models.DateTimeField(default=timezone.datetime.now)
    # 最近一次成功的ping
    ping_last_success_delay = models.FloatField(verbose_name=_("延迟"), null=True, blank=True)
    ping_last_success_fraction_loss = models.FloatField(verbose_name=_("丢包率"), null=True, blank=True)
    ping_last_success_time = models.DateTimeField(verbose_name=_("最后ping通"), null=True, blank=True)

    def ping_last_success_hours(self):
        return "%d" % (((timezone.datetime.now() - self.ping_last_success_time).seconds)/3600)

    def ping_last_success_days(self):
        return (timezone.datetime.now() - self.ping_last_success_time).days

    def _scan(self, ping_timeout=1000, ping_packet=3, smb_timeout=3):
        maxTime, minTime, avrgTime, fracLoss = quiet_ping(hostname=self.ip_address, timeout=ping_timeout, count=ping_packet, path_finder=True)
        if fracLoss < 1.0:
            self.ping_last_success_time = timezone.datetime.now()
            self.ping_last_success_delay = avrgTime
            self.ping_last_success_fraction_loss = fracLoss
        n = NetBIOS()
        try:
            self.hostname = n.queryIPForName(self.ip_address, timeout=smb_timeout)[0]
        except:
            pass
        n.close()
        self.latest_check_time = timezone.datetime.now()
        self.save()

    def __unicode__(self):
        return self.ip_address

    class Meta:
        unique_together = ('ip_address', 'mask')
        verbose_name = _("主机")
        verbose_name_plural = verbose_name

    def get_locale(self):
        return self.subnet.get_locale()
