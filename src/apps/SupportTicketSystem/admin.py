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

class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_short', 'db_active')


class TroubleAdmin(admin.ModelAdmin):
    list_display = ('title', 'for_short', 'db_active')
    filter_horizontal = ['relevant_business', 'relevant_equipment']


class SupportTicketSystemUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_watcher', 'is_worker', 'is_admin', 'db_active')
    list_filter = ('is_watcher', 'is_worker', 'is_admin', 'db_active')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('department', 'contact_name', 'contact_telephone', 'scheduled_time', 'completed', 'responsible_person', 'level', 'start_time', 'db_uuid', 'completed_person')
    list_filter = ('department', 'completed')


admin.site.register(Tag, TagAdmin)
admin.site.register(SupportTicketSystemUser, SupportTicketSystemUserAdmin)
admin.site.register(Trouble, TroubleAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Project)
admin.site.register(ProjectEvent)
admin.site.register(TicketFile)
admin.site.register(ProjectFile)
admin.site.register(ProjectEventFile)
