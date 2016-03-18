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

# Stdlib imports
from redis import Redis
from rq import Queue

# Core Django imports
from django.contrib import admin

# Third-party app imports

# Imports from your apps
from .models import Host, Subnet
from .controller import init_subnet, ping_host, ping_subnet, reverse_host, reverse_subnet

# Register your models here.

redis_conn = Redis()


class SubnetAdmin(admin.ModelAdmin):
    list_display = ('summary', 'subnet_address', 'mask', 'department', 'ping_latest_time', 'reverse_latest_time')
    actions = ['_init_subnet', 'ping', 'reverse']

    def _init_subnet(self, request, queryset):
        q = Queue('low', connection=redis_conn)
        for obj in queryset:
            q.enqueue(init_subnet, obj)
        self.message_user(request, "已加入处理队列，请稍后查询")

    _init_subnet.short_description = "初始化子网"

    def ping(self, request, queryset):
        q = Queue('low', connection=redis_conn)
        for obj in queryset:
            q.enqueue(ping_subnet, obj)
        self.message_user(request, "已加入处理队列，请稍后查询")

    ping.short_description = "Ping"

    def reverse(self, request, queryset):
        q = Queue('low', connection=redis_conn)
        for obj in queryset:
            q.enqueue(reverse_subnet, obj)
        self.message_user(request, "已加入处理队列，请稍后查询")

    reverse.short_description = "ReverseLookup(IP反查计算机名)"


admin.site.register(Subnet, SubnetAdmin)


class HostAdmin(admin.ModelAdmin):
    list_per_page = 300
    list_display = ('ip_address', 'mask', 'subnet', 'description', 'hostname', 'ping_last_success_time', 'ping_latest_time')
    list_filter = ['subnet']
    search_fields = ['ip_address', 'hostname']
    actions = ['ping', 'reverse']

    def ping(self, request, queryset):
        q = Queue('low', connection=redis_conn)
        for obj in queryset:
            q.enqueue(ping_host, obj, save=True)
        self.message_user(request, "已加入处理队列，请稍后查询")

    ping.short_description = "Ping"

    def reverse(self, request, queryset):
        q = Queue('low', connection=redis_conn)
        for obj in queryset:
            q.enqueue(reverse_host, obj, save=True)
        self.message_user(request, "已加入处理队列，请稍后查询")

    reverse.short_description = "ReverseLookup(IP反查计算机名)"





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
