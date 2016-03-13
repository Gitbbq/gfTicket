#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

# Stdlib imports


# Core Django imports
from django.contrib import admin

# Third-party app imports


# Imports from your apps
from .models import DomainSetting, DomainUser


# Register your models here.

class DomainSettingAdmin(admin.ModelAdmin):
    list_display = ('fqdn', 'NetBIOS', 'dc_server', 'search_base')


admin.site.register(DomainSetting, DomainSettingAdmin)


class DomainUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'displayName', 'mail', 'userPrincipalName')


admin.site.register(DomainUser, DomainUserAdmin)
