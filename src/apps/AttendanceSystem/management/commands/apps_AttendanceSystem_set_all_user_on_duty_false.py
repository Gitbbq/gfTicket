#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports
# Core Django imports

from django.core.management.base import BaseCommand
# Third-party app imports

# Imports from your apps

from ...models import AttendanceSystemUser


class Command(BaseCommand):
    help = 'set all user on duty false'

    def handle(self, *args, **options):
        AttendanceSystemUser.objects.filter(on_duty=True).update(on_duty=False)
