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
