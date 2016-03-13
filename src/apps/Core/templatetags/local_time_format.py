#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"
# Stdlib imports
from babel.dates import format_date, format_datetime, format_time
# Core Django imports
from django import template
from django.conf import settings

# Third-party app imports

# Imports from your apps

register = template.Library()

a = settings.LANGUAGE_CODE


def filter_format_date(date, format="medium"):
    return format_date(date, format=format, locale='zh_CN')


def filter_format_time(time, format="a h:m"):
    if time is None:
        return "-"
    return format_time(time, locale='zh_CN', format=format)


def filter_format_datetime(datetime, format="a h:m"):
    if datetime is None:
        return "-"
    return format_datetime(datetime, locale='zh_CN', format=format)


register.filter('format_date', filter_format_date)
register.filter('format_time', filter_format_time)
register.filter('format_datetime', filter_format_datetime)
