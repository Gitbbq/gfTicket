#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'lian'
# __email__ = "liantian@188.com"

# Stdlib imports
import uuid
import hashlib
import mimetypes
import os
# Core Django imports
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Third-party app imports


# Imports from your apps


# Create your models here.

class CommonModel(models.Model):
    """
    An abstract base class model that provides self-
    updating ``created`` and ``modified`` fields.
    """
    db_created = models.DateTimeField(auto_now_add=True, verbose_name=_("创建日期"), db_index=True)
    db_modified = models.DateTimeField(auto_now=True, verbose_name=_("修改日期"), db_index=True)
    db_uuid = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True)
    db_manual_order = models.FloatField(verbose_name="顺位", default=0.0, db_index=True, editable=False)
    db_active = models.BooleanField(default=True, verbose_name=_("激活"), db_index=True)

    def __unicode__(self):
        return str(self.db_uuid)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        abstract = True
        ordering = ['db_manual_order']


class DownloadModel(CommonModel):
    save_path = 'download'

    def upload_dir(instance, filename):
        return '%s/%s/%s' % (instance.save_path, str(instance.db_uuid), filename)

    # use the custom storage class fo the FileField
    filename = models.CharField(max_length=255, verbose_name=_('文件名'), null=True, editable=False)
    content_type = models.CharField(max_length=127, verbose_name=_('Content Type'), null=True, editable=False)
    orig_file = models.FileField(upload_to=upload_dir, verbose_name=_("文件"), help_text=_("选择一个文件并上传"))
    md5sum = models.CharField(max_length=36, null=True, editable=False)
    manual = models.TextField(blank=True, null=True, verbose_name=_("说明"))

    def save(self, *args, **kwargs):
        if not self.pk:  # file is new
            self.filename = os.path.basename(self.orig_file.name)
            mime_type = mimetypes.guess_type(self.filename)[0]
            if mime_type is None:
                self.content_type = "application/octet-stream"
            else:
                self.content_type = mime_type
            md5 = hashlib.md5()
            for chunk in self.orig_file.chunks():
                md5.update(chunk)
            self.md5sum = md5.hexdigest()
        super(DownloadModel, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.filename

    class Meta:
        abstract = True
