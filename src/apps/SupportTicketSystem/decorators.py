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
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _

# Third-party app imports

# Imports from your apps
from .models import SupportTicketSystemUser


def has_support_ticket_system_user(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            try:
                support_ticket_system_user = (request.user.support_ticket_system_user is not None)
            except SupportTicketSystemUser.DoesNotExist:
                return HttpResponseRedirect(reverse(viewname="SupportTicketSystem:initialize_user") + "?next=" + request.path)
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def verified_support_ticket_system_user_is_worker(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            if request.user.support_ticket_system_user.is_worker is False:
                return HttpResponseRedirect(reverse(viewname="SupportTicketSystem:error") + "?error=" + _("当前用户不是工作用户"))
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def verified_support_ticket_system_user_is_admin(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            # attendance_system_user, created = AttendanceSystemUser.objects.get_or_create(user=request.user)
            if request.user.support_ticket_system_user.is_admin is False:
                return HttpResponseRedirect(reverse(viewname="SupportTicketSystem:error") + "?error=" + _("当前用户不是管理员"))
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def verified_support_ticket_system_user_is_watcher(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            # attendance_system_user, created = AttendanceSystemUser.objects.get_or_create(user=request.user)
            if request.user.support_ticket_system_user.is_watcher is False:
                return HttpResponseRedirect(reverse(viewname="SupportTicketSystem:error") + "?error=" + _("当前用户不是值班员"))
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)
