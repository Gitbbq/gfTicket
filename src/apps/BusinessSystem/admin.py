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

class SystemAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_short', 'url', 'bs', 'cs', 'developer', 'db_active')
    list_filter = ('bs', 'cs', 'developer', 'db_active')


#
#
# admin.site.register(EquipmentBrand)
# admin.site.register(EquipmentType)
admin.site.register(System, SystemAdmin)
