#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Liantian'
__email__ = "liantian@188.com"
# Stdlib imports
# Core Django imports
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _

# Third-party app imports

# Imports from your apps
from .models import AttendanceSystemUser


def has_attendance_system_user(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            try:
                attendance_system_user = (request.user.attendance_system_user is not None)
            except AttendanceSystemUser.DoesNotExist:
                return HttpResponseRedirect(reverse(viewname="AttendanceSystem:initialize_user") + "?next=" + request.path)
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def verified_attendance_system_is_worker(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            # attendance_system_user, created = AttendanceSystemUser.objects.get_or_create(user=request.user)
            if request.user.attendance_system_user.is_worker is False:
                return HttpResponseRedirect(reverse(viewname="AttendanceSystem:error") + "?error=" + _("当前用户不是签到系统用户"))
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)


def verified_attendance_system_is_admin(function=None):
    def _dec(view_func):
        def _view(request, *args, **kwargs):
            # attendance_system_user, created = AttendanceSystemUser.objects.get_or_create(user=request.user)
            if request.user.attendance_system_user.is_admin is False:
                return HttpResponseRedirect(reverse(viewname="AttendanceSystem:error") + "?error=" + _("当前用户不是签到系统管理员"))
            return view_func(request, *args, **kwargs)

        _view.__name__ = view_func.__name__
        _view.__dict__ = view_func.__dict__
        _view.__doc__ = view_func.__doc__

        return _view

    if function is None:
        return _dec
    else:
        return _dec(function)
