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
