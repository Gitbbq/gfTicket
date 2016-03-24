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

# Core Django imports

from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator

# Third-party app imports
from apps.Core.views import BaseView
from apps.SSO.decorators import verified_required
# Imports from your apps

from .models import AttendanceSystemUser
from .models import Entry
from .decorators import verified_attendance_system_is_worker
from .decorators import has_attendance_system_user
from .decorators import verified_attendance_system_is_admin


class Error(BaseView):
    template_name = "AttendanceSystem/error.html"

    def get(self, request):
        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
class InitializeUser(BaseView):
    template_name = "AttendanceSystem/initialize_user.html"

    def get(self, request):
        attendance_system_user, created = AttendanceSystemUser.objects.get_or_create(user=request.user)
        attendance_system_user.save()
        return self.go_next()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_attendance_system_user, name='dispatch')
@method_decorator(verified_attendance_system_is_worker, name='dispatch')
class Myself(BaseView):
    template_name = "AttendanceSystem/myself.html"

    def get(self, request, check_out=False):
        attendance_system_user = AttendanceSystemUser.objects.get(user=request.user)
        current_entry, created = Entry.objects.get_or_create(user=attendance_system_user,
                                                             date=timezone.now())

        if check_out:
            attendance_system_user.on_duty = False
            current_entry.last_time = timezone.now()
            current_entry.last_time_ip = request.META.get("REMOTE_ADDR", "192.168.1.1")
        else:
            if current_entry.first_time_ip is None:
                current_entry.first_time_ip = request.META.get("REMOTE_ADDR", "192.168.1.1")
            attendance_system_user.on_duty = True

        current_entry.save()
        attendance_system_user.save()

        my_entries = Entry.objects.filter(user=attendance_system_user).all()[:50]

        self.response_dict['attendance_system_user'] = attendance_system_user
        self.response_dict['my_entries'] = my_entries

        return self.response()


@method_decorator(login_required, name='dispatch')
class OnDuty(BaseView):
    template_name = "AttendanceSystem/on_duty.html"

    def get(self, request):
        workers = AttendanceSystemUser.objects.filter(is_worker=True).all()
        self.response_dict['workers'] = workers
        return self.response()


@method_decorator(login_required, name='dispatch')
@method_decorator(verified_required, name='dispatch')
@method_decorator(has_attendance_system_user, name='dispatch')
@method_decorator(verified_attendance_system_is_admin, name='dispatch')
class AdminView(BaseView):
    template_name = "AttendanceSystem/admin_view.html"

    def get(self, request):
        self.response_dict['entries'] = Entry.objects.filter(date__gte=timezone.datetime.today() - timezone.timedelta(days=62)).all()
        self.response_dict['workers'] = AttendanceSystemUser.objects.filter(is_worker=True).all()
        return self.response()
