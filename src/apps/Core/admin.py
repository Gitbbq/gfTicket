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
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

# Third-party app imports


# Imports from your apps
from apps.AttendanceSystem.models import AttendanceSystemUser
from apps.Document.models import DocumentUser
from apps.SupportTicketSystem.models import SupportTicketSystemUser
from apps.DayBook.models import DayBookUser


# Register your models here.

class DayBookUserInline(admin.StackedInline):
    model = DayBookUser
    max_num = 1
    can_delete = False


class AttendanceSystemUserInline(admin.StackedInline):
    model = AttendanceSystemUser
    max_num = 1
    can_delete = False


class DocumentUserInline(admin.StackedInline):
    model = DocumentUser
    max_num = 1
    can_delete = False


class SupportTicketSystemUserInline(admin.StackedInline):
    model = SupportTicketSystemUser
    max_num = 1
    can_delete = False


class UserAdmin(AuthUserAdmin):
    inlines = [AttendanceSystemUserInline, DocumentUserInline, SupportTicketSystemUserInline, DayBookUserInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
