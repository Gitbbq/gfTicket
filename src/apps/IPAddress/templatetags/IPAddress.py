#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"
# Stdlib imports

# Core Django imports
from django import template
from django.utils.translation import ugettext_lazy as _
# Third-party app imports

# Imports from your apps
from ..models import Host

register = template.Library()


def ip_to_department(ip_address):
    try:
        host = Host.objects.get(ip_address=ip_address)
        return host.subnet.department.title
    except:
        return _("无法判断地址来源")


register.filter('ip_to_department', ip_to_department)
