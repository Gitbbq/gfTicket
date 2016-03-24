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

# Core Django imports
from django import template
from django.utils import timezone

# Third-party app imports

# Imports from your apps

register = template.Library()


def time_in_range(x, args="16:30,18:30"):
    if x is None:
        return False
    q = args.split(',')
    start = timezone.datetime.strptime(q[0], "%H:%M").time()
    end = timezone.datetime.strptime(q[1], "%H:%M").time()
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


register.filter('time_in_range', time_in_range)
