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
import jieba.analyse
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
from apps.BusinessSystem.models import System as BusinessSystem
from apps.Equipment.models import EquipmentModel

# Create your models here.
TYPE_CHOICES = (
    ('system ', _(u"系统配置手册")),
    ('debug', _(u"排错")),
    ('page', _(u"页面")),
)

STATUS_CHOICES = (
    ('published', _(u"已发布")),
    ('draft', _(u"草稿")),
    ('trash', _(u"回收站")),
)

COMMENT_STATUS_CHOICES = (
    ('yes', _(u"可以评论")),
    ('no', _(u"禁止评论")),
)

BS_CSS_STYLE = (
    ('default', _(u"默认")),
    ('primary', _(u"primary")),
    ('success', _(u"success")),
    ('info', _(u"info")),
    ('warning', _(u"warning")),
    ('danger', _(u"danger")),
)

PERMISSION_CHOICES = (
    (0, _(u"访客")),
    (1, _(u"一般权限")),
    (2, _(u"高级权限")),
)


class Tag(CommonModel):
    title = models.CharField(verbose_name=_(u"标题"), max_length=255)
    count = models.IntegerField(editable=False, default=0)

    class Meta:
        verbose_name = _(u"Tag")
        verbose_name_plural = verbose_name

    def update_count(self):
        self.count = self.entries.filter(db_active=True).count()
        self.save()

    def __unicode__(self):
        return self.title


class Entry(CommonModel):
    title = models.CharField(verbose_name=_(u"标题"), max_length=255)
    content = models.TextField(verbose_name=_(u"正文"))
    content_less = models.TextField(verbose_name=_(u"简单正文"), blank=True)
    type = models.CharField(verbose_name=_(u"类型"), choices=TYPE_CHOICES, default="blog", max_length=255)
    status = models.CharField(verbose_name=_(u"状态"), choices=STATUS_CHOICES, default="published", max_length=255)
    comment_status = models.CharField(verbose_name=_(u"是否允许评论"), choices=COMMENT_STATUS_CHOICES, default="yes", max_length=255)

    # category = models.ForeignKey(to=Category, verbose_name=_(u"分类"), blank=True, null=True, related_name='entries')
    tag = models.ManyToManyField(to=Tag, verbose_name=_("Tags"), related_name="entries", blank=True)

    key_word = ArrayField(models.CharField(max_length=200), blank=True, editable=False)
    record = JSONField(default={"history": []}, verbose_name=_("历史记录"), blank=True, editable=False)

    require_permission = models.IntegerField(default=0, verbose_name=_('所需权限'), choices=PERMISSION_CHOICES)

    # relevant_system = models.ManyToManyField(to=BusinessSystem, verbose_name=_("相关系统"), blank=True, related_name='relevant_doc')

    css_style = models.CharField(verbose_name=_(u"css样式"), choices=BS_CSS_STYLE, default="default", max_length=255)

    # 相关
    relevant_business = models.ManyToManyField(BusinessSystem, verbose_name=_("涉及系统"), related_name="relevant_document", blank=True,
                                               help_text=_('涉及的业务系统，没有请留空'))
    relevant_equipment = models.ManyToManyField(EquipmentModel, verbose_name=_("涉及硬件"), related_name="relevant_document", blank=True,
                                                help_text=_('涉及的硬件设备类型，请尽量准确，没有请留空'))

    def save(self, *args, **kwargs):
        self.key_word = jieba.analyse.textrank(self.content, topK=15)
        self.record.setdefault("history", []).append({"time": timezone.datetime.now().isoformat(), "content": self.content, "content_less": self.content_less})
        super(Entry, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _(u"文章")
        verbose_name_plural = verbose_name
        ordering = ['-db_manual_order', '-db_modified']

    def __unicode__(self):
        return self.title


class DocumentUser(CommonModel):
    user = models.OneToOneField(User, verbose_name=_("对应用户"), related_name="document_user")
    permission = models.IntegerField(default=0, verbose_name=_('拥有权限'), choices=PERMISSION_CHOICES)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name = _("文档系统用户")
        verbose_name_plural = verbose_name
