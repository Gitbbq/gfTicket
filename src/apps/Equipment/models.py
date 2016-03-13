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


class EquipmentType(CommonModel):
    # use the custom storage class fo the FileField
    title = models.CharField(max_length=255, verbose_name=_('设备类型'))
    for_short = models.CharField(max_length=24, default=" ", verbose_name=_("缩写"))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("设备类型")
        verbose_name_plural = verbose_name


class EquipmentBrand(CommonModel):
    # use the custom storage class fo the FileField
    title = models.CharField(max_length=255, verbose_name=_('设备品牌'))
    for_short = models.CharField(max_length=24, default=" ", verbose_name=_("缩写"))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("设备品牌")
        verbose_name_plural = verbose_name


class EquipmentModel(CommonModel):
    # use the custom storage class fo the FileField
    title = models.CharField(max_length=255, verbose_name=_('设备型号'))
    brand = models.ForeignKey(to=EquipmentBrand, verbose_name=_("品牌"))
    type = models.ForeignKey(to=EquipmentType, verbose_name=_("设备类型"))

    def __unicode__(self):
        return "%s[%s]-%s[%s]-%s" % (self.type.title, self.type.for_short, self.brand.title, self.brand.for_short, self.title)

    class Meta:
        verbose_name = _("设备型号")
        verbose_name_plural = verbose_name

    def public_documents(self):
        return self.relevant_document.filter(require_permission=0).filter(db_active=True).all()

    def public_downloads(self):
        return self.driver.filter(db_active=True).all()
