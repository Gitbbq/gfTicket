# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 22:56
from __future__ import unicode_literals

from django.db import migrations, models

import apps.DownloadCenter.models


class Migration(migrations.Migration):
    dependencies = [
        ('DownloadCenter', '0007_auto_20160202_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='orig_file',
            field=models.FileField(help_text='选择一个文件并上传', upload_to=apps.DownloadCenter.models.DownloadModel.upload_dir, verbose_name='文件'),
        ),
    ]
