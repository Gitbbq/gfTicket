#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
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
