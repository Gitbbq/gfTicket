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
import os

from redis import Redis
from rq import Queue

# Core Django imports


from django.core.management.base import BaseCommand
# Third-party app imports

# Imports from your apps

from ...models import Subnet
from ...controller import scan_subnet

redis_conn = Redis()


class Command(BaseCommand):
    help = 'scan Host'

    def handle(self, *args, **options):
        q = Queue('scan_subnet', connection=redis_conn)
        q.empty()
        all_subnet = Subnet.objects.order_by("latest_scan_time").all()
        for subnet in all_subnet:
            q.enqueue(scan_subnet, subnet, max_workers=(os.cpu_count() or 1) * 10)
