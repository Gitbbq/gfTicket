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
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Third-party app imports


# Imports from your apps
from apps.Core.models import CommonModel


# Create your models here.

class AttendanceSystemUser(CommonModel):
    user = models.OneToOneField(User, verbose_name=_("对应用户"), related_name="attendance_system_user")
    is_worker = models.BooleanField(default=False, verbose_name=_('激活考勤系统签到权限'))
    is_admin = models.BooleanField(default=False, verbose_name=_('激活考勤系统管理员权限'))
    on_duty = models.BooleanField(default=False, verbose_name=_("在岗"))

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = _("考勤系统用户")
        verbose_name_plural = verbose_name

    def today_first_time(self):
        return Entry.objects.get(user=self, date=timezone.datetime.today()).first_time

    def today_last_time(self):
        return Entry.objects.get(user=self, date=timezone.datetime.today()).last_time


class Entry(CommonModel):
    user = models.ForeignKey(to=AttendanceSystemUser, verbose_name=_("用户"), related_name="entries")
    date = models.DateField(verbose_name=_("日期"))
    first_time = models.TimeField(verbose_name=_("首次时间"), default=timezone.now)
    last_time = models.TimeField(verbose_name=_("最后一次的时间"), null=True)
    # first_time_local = models.CharField(verbose_name=_("签到地点"), default=" ", max_length=127)
    # last_time_local = models.CharField(verbose_name=_("签退地点"), default=" ", max_length=127)
    first_time_ip = models.GenericIPAddressField(verbose_name=_("首次IP"), null=True, blank=True)
    last_time_ip = models.GenericIPAddressField(verbose_name=_("签退IP"), null=True, blank=True)

    def __unicode__(self):
        return self.user.user.username

    class Meta:
        verbose_name = _("考勤记录")
        verbose_name_plural = verbose_name
        unique_together = (("user", "date"),)
        ordering = ["-date"]

    def weekday(self):
        weekday_dict = {
            0: _("星期一"),
            1: _("星期二"),
            2: _("星期三"),
            3: _("星期四"),
            4: _("星期五"),
            5: _("星期六"),
            6: _("星期日"),
        }
        return weekday_dict[self.date.weekday()]
