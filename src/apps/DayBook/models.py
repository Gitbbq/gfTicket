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
# import jieba.analyse
# Core Django imports
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
# Third-party app imports


# Imports from your apps
from apps.Core.models import CommonModel
from apps.BranchManager.models import Department


# Create your models here.

class DayBookUser(CommonModel):
    user = models.OneToOneField(User, verbose_name=_("对应用户"), related_name="daybook_user")
    internet_pc_add = models.BooleanField(default=False, verbose_name=_('添加外网机'))
    internet_pc_edit = models.BooleanField(default=False, verbose_name=_('修改外网机'))

    def __unicode__(self):
        try:
            result = self.user.sso_user.displayName
            result = result.split("/")[0]
            if result is None:
                result = self.user.get_full_name()
        except:
            result = self.user.get_full_name()
        return result

    class Meta:
        verbose_name = _("台帐用户")
        verbose_name_plural = verbose_name


class InternetPC(CommonModel):
    case_sn = models.CharField(max_length=128, verbose_name=_("主机序列号"), null=True, blank=True)
    screen_sn = models.CharField(max_length=128, verbose_name=_("显示器序列号"), null=True, blank=True)
    ip_address = models.GenericIPAddressField(verbose_name=_("IP地址"), null=True, blank=True)
    hostname = models.CharField(max_length=128, verbose_name=_("主机名"), null=True, blank=True)
    department = models.ForeignKey(to=Department, limit_choices_to={"db_active": True}, verbose_name=_("网点"), related_name="internet_pc")
    description = models.TextField(verbose_name=_("详细描述"), null=True, blank=True)
    manager = models.CharField(max_length=128, verbose_name=_("管理者"), null=True, blank=True)
    way = models.CharField(max_length=128, verbose_name=_("上网方式"), default="eth", choices=(('adsl', _('ADSL')), ('eth', _('代理内网')),))

    class Meta:
        verbose_name = _(u"外网机")
        verbose_name_plural = verbose_name
        ordering = ['-db_manual_order', '-db_modified']


class InternetPCLog(CommonModel):
    pc = models.ForeignKey(to=InternetPC, related_name="log")
    user = models.ForeignKey(to=User)
    history = JSONField(verbose_name=_("历史"), editable=False)
