#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

# Create your models here.

# Stdlib imports

# Core Django imports
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# Third-party app imports


# Imports from your apps
from .models import *


# Register your models here.

class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('filename', 'content_type', 'orig_file', 'md5sum', 'db_uuid')


admin.site.register(Attachment, AttachmentAdmin)


class DriverAdmin(admin.ModelAdmin):
    list_display = ('filename', 'type', 'brand', 'get_equipment_model_list', 'os_compatibility', 'orig_file', 'db_uuid')
    filter_horizontal = ["equipment_model"]

    def get_equipment_model_list(self, obj):
        return ",\n".join([p.title for p in obj.equipment_model.all()])

    get_equipment_model_list.short_description = _("匹配设备")


admin.site.register(Driver, DriverAdmin)


class BusinessSoftwareAdmin(admin.ModelAdmin):
    list_display = ('filename', 'system', 'manual', 'orig_file', 'md5sum', 'db_uuid')


admin.site.register(BusinessSoftware, BusinessSoftwareAdmin)
