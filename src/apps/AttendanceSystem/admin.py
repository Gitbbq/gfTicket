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

class AttendanceSystemUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_worker', 'is_admin']


class EntryAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'first_time', 'last_time']
    list_filter = ['user']


admin.site.register(AttendanceSystemUser, AttendanceSystemUserAdmin)
admin.site.register(Entry, EntryAdmin)
