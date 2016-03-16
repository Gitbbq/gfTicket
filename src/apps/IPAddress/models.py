#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+code@gmail.com"
#
# Copyright 2015-2016 liantian
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

# Create your models here.

# Stdlib imports
import ipaddress

# Core Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

# Third-party app imports


# Imports from your apps
from apps.Core.models import CommonModel
from apps.BranchManager.models import Department


class Subnet(CommonModel):
    subnet_address = models.GenericIPAddressField(verbose_name=_("子网地址"))
    mask = models.GenericIPAddressField(verbose_name=_("子网掩码"), default="255.255.255.0")

    gateway = models.GenericIPAddressField(verbose_name=_("网关"), null=True, blank=True)
    vlan = models.IntegerField(verbose_name=_("VLAN ID"), default=1)

    department = models.ForeignKey(to=Department, verbose_name=_("部门"), related_name="subnet", null=True, blank=True)

    summary = models.CharField(max_length=128, verbose_name=_("简介"), default="None")
    description = models.TextField(max_length=255, blank=True, verbose_name=_("详细描述"), default="None")

    been_init = models.BooleanField(default=False, editable=False)

    latest_scan_time = models.DateTimeField(default=timezone.datetime.now, verbose_name=_("最后扫描时间"))

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
    # ping_last_success_fraction_loss = models.FloatField(verbose_name=_("丢包率"), null=True, blank=True)
    ping_last_success_time = models.DateTimeField(verbose_name=_("最后ping通"), null=True, blank=True)

    def latest_scan_time_hours(self):
        return ((timezone.datetime.now() - self.latest_scan_time).total_seconds()) / 3600

    def latest_scan_time_minute(self):
        return ((timezone.datetime.now() - self.latest_scan_time).total_seconds()) / 60

    def ping_last_success_minute(self):
        return ((timezone.datetime.now() - self.ping_last_success_time).total_seconds()) / 60

    def ping_last_success_hours(self):
        return ((timezone.datetime.now() - self.ping_last_success_time).total_seconds()) / 3600

    def ping_last_success_days(self):
        return ((timezone.datetime.now() - self.ping_last_success_time).total_seconds()) / 86400

    def __unicode__(self):
        return self.ip_address

    class Meta:
        unique_together = ('ip_address', 'mask')
        verbose_name = _("主机")
        verbose_name_plural = verbose_name

    def get_locale(self):
        return self.subnet.get_locale()
