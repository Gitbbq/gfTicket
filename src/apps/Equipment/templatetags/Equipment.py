#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"
# Stdlib imports
# Core Django imports
from django import template

# Third-party app imports

# Imports from your apps

register = template.Library()




# def filter_format_date(date, format="medium"):
#     return format_date(date, format=format, locale='zh_CN')
#
#
# def filter_format_time(time, format="a h:m"):
#     if time is None:
#         return "-"
#     return format_time(time, locale='zh_CN',format=format)
#
#
# register.filter('format_date', filter_format_date)
# register.filter('format_time', filter_format_time)
