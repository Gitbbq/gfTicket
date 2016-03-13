#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports

# Core Django imports
from django.utils.translation import ugettext as _
# Third-party app imports

# Imports from your apps

from .models import Host


def ip_to_department(ip_address):
    try:
        host = Host.objects.get(ip_address=ip_address)
        return host.subnet.department.title
    except:
        return _("无法判断地址来源")
