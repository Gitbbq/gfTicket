#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports
from rq import Queue
from redis import Redis
# Core Django imports

from django.core.management.base import BaseCommand
# Third-party app imports

# Imports from your apps

from ...models import Subnet

redis_conn = Redis()


class Command(BaseCommand):
    help = 'Init one Subnet which been_init=False'

    def handle(self, *args, **options):
        q = Queue('low', connection=redis_conn)
        queryset = Subnet.objects.filter(been_init=False).all()
        for obj in queryset:
            q.enqueue(obj._init_hosts)
