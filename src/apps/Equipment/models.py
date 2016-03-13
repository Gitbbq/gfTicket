#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

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
