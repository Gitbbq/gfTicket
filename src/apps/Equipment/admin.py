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

# class AttachmentAdmin(admin.ModelAdmin):
#     list_display = ('filename', 'content_type', 'orig_file', 'md5sum', 'db_uuid')
#
#

class EquipmentModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'type', 'db_active')
    list_filter = ('brand', 'type', 'db_active')


class EquipmentBrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_short', 'db_active')


class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_short', 'db_active')


admin.site.register(EquipmentBrand, EquipmentBrandAdmin)
admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(EquipmentModel, EquipmentModelAdmin)
