#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'lian'
__email__ = "liantian@188.com"

# Stdlib imports
from rq import Queue
from redis import Redis

# Core Django imports
from django.contrib import admin

# Third-party app imports

# Imports from your apps
from .models import Host, Subnet

# Register your models here.

redis_conn = Redis()


class SubnetAdmin(admin.ModelAdmin):
    list_display = ('summary', 'subnet_address', 'mask', 'department')
    actions = ['init_hosts']

    def init_hosts(self, request, queryset):
        q = Queue('low', connection=redis_conn)
        for obj in queryset:
            q.enqueue(obj._init_hosts)
        self.message_user(request, "已加入处理队列，请稍后查询")

    init_hosts.short_description = "初始化子网"


admin.site.register(Subnet, SubnetAdmin)


class HostAdmin(admin.ModelAdmin):
    list_per_page = 300
    list_display = ('ip_address', 'mask', 'subnet', 'description', 'hostname', 'ping_last_success_time', 'ping_last_success_delay', 'latest_scan_time')
    list_filter = ['subnet']
    search_fields = ['ip_address', 'hostname']
    actions = ['scan']

    def scan(self, request, queryset):
        q = Queue('low', connection=redis_conn)
        for obj in queryset:
            q.enqueue(obj._scan)
        self.message_user(request, "已加入处理队列，请稍后查询")

    scan.short_description = "扫描延迟和主机名"



    # def ping_hosts(self, request, queryset):
    #     for obj in queryset:
    #         obj.make_ping(level="default")
    #     self.message_user(request, "已加入处理队列，请稍后查询")
    # ping_hosts.short_description = "Ping 测试"
    #
    # def get_hostname(self, request, queryset):
    #     for obj in queryset:
    #         obj.get_hostname(level="default")
    #     self.message_user(request, "已加入处理队列，请稍后查询")
    # get_hostname.short_description = "获取主机名"


admin.site.register(Host, HostAdmin)
