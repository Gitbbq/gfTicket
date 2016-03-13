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
