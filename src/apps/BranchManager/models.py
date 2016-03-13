#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

# Create your models here.

# Stdlib imports

# Core Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Third-party app imports


# Imports from your apps
from apps.Core.models import CommonModel


# Create your models here.

class Area(CommonModel):
    title = models.CharField(max_length=255, verbose_name=_("标题"), unique=True)
    description = models.TextField(blank=True, verbose_name=_("详细描述"))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("地理区域")
        verbose_name_plural = verbose_name

    def active_departments(self):
        return self.department_set.filter(db_active=True).all()


class DepartmentType(CommonModel):
    title = models.CharField(max_length=255, verbose_name=_("标题"), unique=True)
    description = models.TextField(blank=True, verbose_name=_("详细描述"))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _("部门分类")
        verbose_name_plural = verbose_name

    def active_departments(self):
        return self.department_set.filter(db_active=True).all()


class Department(CommonModel):
    title = models.CharField(max_length=255, verbose_name=_("标题"), unique=True)
    for_short = models.CharField(max_length=255, verbose_name=_("缩写"))
    pinyin = models.CharField(max_length=255, verbose_name=_("拼音"))
    dot_code = models.CharField(max_length=255, verbose_name=_("网点号"), unique=True)
    description = models.TextField(blank=True, verbose_name=_("详细描述"))
    area = models.ForeignKey(to=Area, verbose_name=_("所在区域"))
    type = models.ForeignKey(to=DepartmentType, verbose_name=_("部门分类"))

    def __unicode__(self):
        return "%s-%s (%s)  |%s|%s|" % (self.dot_code, self.title, self.type.title, self.for_short, self.pinyin)

    class Meta:
        verbose_name = _("部门/网点")
        verbose_name_plural = verbose_name


class SubDepartment(CommonModel):
    title = models.CharField(max_length=255, verbose_name=_("标题"), unique=True)
    for_short = models.CharField(max_length=255, verbose_name=_("缩写"))
    description = models.TextField(blank=True, verbose_name=_("详细描述"))
    parent = models.ForeignKey(to=Department, verbose_name=_("父级部门"))

    def __unicode__(self):
        return self.ip_address

    class Meta:
        verbose_name = _("二级部门")
        verbose_name_plural = verbose_name

    def type(self):
        return self.parent.type
