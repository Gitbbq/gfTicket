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
