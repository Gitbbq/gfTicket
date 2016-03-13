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
from datetime import datetime, timedelta
from rq import Queue
from redis import Redis
# Core Django imports


from django.core.management.base import BaseCommand
# Third-party app imports

# Imports from your apps

from ...models import Host

redis_conn = Redis()


class Command(BaseCommand):
    help = 'scan Host'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('--count', '-c', default=500, type=int, dest='count')

    def handle(self, *args, **options):
        q = Queue('scan_host', connection=redis_conn)
        q.empty()
        count = options['count']
        hosts = Host.objects.order_by("latest_scan_time")[:count]
        for host in hosts:
            q.enqueue(host._scan)
