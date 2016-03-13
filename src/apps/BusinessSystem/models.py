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
