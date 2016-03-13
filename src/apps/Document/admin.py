#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

# Create your models here.

# Stdlib imports

# Core Django imports
from django.contrib import admin

# Third-party app imports


# Imports from your apps
from .models import *


# Register your models here.


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'count')


admin.site.register(Tag, TagAdmin)


class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'db_uuid')
    filter_horizontal = ['tag', 'relevant_business', 'relevant_equipment']


admin.site.register(Entry, EntryAdmin)
admin.site.register(DocumentUser)
