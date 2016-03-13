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

class AreaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class DepartmentTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["title", 'dot_code', 'for_short', 'area', 'type', 'for_short', 'db_active']
    list_filter = ['area', 'type', 'db_active']


class SubDepartmentAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', 'parent', 'for_short']
    list_filter = ['parent']


admin.site.register(Area, AreaAdmin)
admin.site.register(DepartmentType, DepartmentTypeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(SubDepartment, SubDepartmentAdmin)
