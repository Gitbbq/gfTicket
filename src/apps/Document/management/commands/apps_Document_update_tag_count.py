#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'Liantian'
# __email__ = "liantian.me+noreply@gmail.com"
# Stdlib imports
# Core Django imports

from django.core.management.base import BaseCommand
# Third-party app imports

# Imports from your apps

from ...models import Tag


class Command(BaseCommand):
    help = 'Update the tags count.'

    def handle(self, *args, **options):
        tags = Tag.objects.filter(db_active=True).all()
        for tag in tags:
            tag.update_count()
