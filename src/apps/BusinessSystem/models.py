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
from django.utils.translation import ugettext_lazy as _
# Third-party app imports


# Imports from your apps
from apps.Core.models import CommonModel


# Create your models here.


class System(CommonModel):
    # use the custom storage class fo the FileField
    title = models.CharField(max_length=255, verbose_name=_('标题'))
    for_short = models.CharField(max_length=24, default=" ", verbose_name=_("缩写"))
    url = models.URLField(verbose_name=_('网址'), blank=True, null=True)
    bs = models.BooleanField(verbose_name=_('B/S系统'), default=False)
    cs = models.BooleanField(verbose_name=_('C/S系统'), default=False)
    developer = models.CharField(verbose_name=_("开发商"), max_length=127, choices=(
        ('zoh', _("总行")),
        ('bej', _("北京分行")),
        ('YJH', _("银监")),
        ('RH', _("人行")),
        ('third', _("第三方")),
    ))

    def __unicode__(self):
        return '%s[%s]' % (self.title, self.for_short)

    class Meta:
        verbose_name = _("系统")
        verbose_name_plural = verbose_name

    def public_documents(self):
        return self.relevant_document.filter(require_permission=0).filter(db_active=True).all()

    def public_downloads(self):
        return self.software.filter(db_active=True).all()

# class EquipmentBrand(CommonModel):
#     # use the custom storage class fo the FileField
#     title = models.CharField(max_length=255, verbose_name=_('设备品牌'))
#
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = _("设备品牌")
#         verbose_name_plural = verbose_name
#
#
# class EquipmentModel(CommonModel):
#     # use the custom storage class fo the FileField
#     title = models.CharField(max_length=255, verbose_name=_('设备型号'))
#     brand = models.ForeignKey(to=EquipmentBrand, verbose_name=_("品牌"))
#     type = models.ForeignKey(to=EquipmentType, verbose_name=_("设备类型"))
#
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = _("设备型号")
#         verbose_name_plural = verbose_name
