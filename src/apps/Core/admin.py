#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

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


# Register your models here.


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
    inlines = [AttendanceSystemUserInline, DocumentUserInline, SupportTicketSystemUserInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
