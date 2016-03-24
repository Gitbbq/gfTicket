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
# Stdlib imports
import ipaddress
# Core Django imports
from django import template
from django.utils.translation import ugettext_lazy as _
# Third-party app imports

# Imports from your apps
from ..models import Host

register = template.Library()


def ip_to_department(ip_address):
    if ip_address is None:
        return  _("无")
    try:
        host = Host.objects.get(ip_address=ip_address)
        return host.subnet.department.title
    except:
        return _("无法判断地址来源")


def ip_sn(ip_address):
    ip = ipaddress.ip_address(ip_address)
    if ip.version == 4:
        return ip.__str__().split(".")[-1]
    elif ip.version == 6:
        return ip.exploded.__str__().strip(":")[-1]
    else:
        return "0"


register.filter('ip_to_department', ip_to_department)
register.filter('ip_sn', ip_sn)
