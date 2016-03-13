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
import hashlib
import mimetypes
import os

# Core Django imports
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Third-party app imports


# Imports from your apps
from apps.Core.models import CommonModel, DownloadModel
from apps.Equipment.models import EquipmentModel, EquipmentBrand, EquipmentType
from apps.BusinessSystem.models import System as BusinessSystem


# Create your models here.


class Attachment(DownloadModel):
    save_path = 'attachment'

    class Meta:
        verbose_name = _("附件")
        verbose_name_plural = verbose_name


class Driver(DownloadModel):
    save_path = 'driver'
    # use the custom storage class fo the FileField
    brand = models.ForeignKey(to=EquipmentBrand, verbose_name=_("品牌"))
    type = models.ForeignKey(to=EquipmentType, verbose_name=_("设备类型"))
    equipment_model = models.ManyToManyField(to=EquipmentModel, verbose_name=_("适配设备型号"), related_name="driver")
    os_compatibility = models.CharField(verbose_name=_("兼容性"), max_length=127, choices=(
        ('32', _("32位")),
        ('64', _("64位")),
        ('all', _("通用")),
    ))

    def get_equipment_model_list(self):
        return " , ".join([p.title for p in self.equipment_model.all()])

    class Meta:
        verbose_name = _("驱动程序")
        verbose_name_plural = verbose_name


class BusinessSoftware(DownloadModel):
    save_path = 'business_software'
    system = models.ForeignKey(to=BusinessSystem, verbose_name=_("业务系统"), related_name="software")

    class Meta:
        verbose_name = _("业务软件")
        verbose_name_plural = verbose_name
