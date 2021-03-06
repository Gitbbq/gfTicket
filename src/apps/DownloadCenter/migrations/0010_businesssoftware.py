# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 23:08
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models

import apps.DownloadCenter.models


class Migration(migrations.Migration):
    dependencies = [
        ('BusinessSystem', '0001_initial'),
        ('DownloadCenter', '0009_auto_20160202_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessSoftware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(default=0.0, verbose_name='顺位')),
                ('filename', models.CharField(editable=False, max_length=255, null=True, verbose_name='文件名')),
                ('content_type', models.CharField(editable=False, max_length=127, null=True, verbose_name='Content Type')),
                ('orig_file', models.FileField(help_text='选择一个文件并上传', upload_to=apps.DownloadCenter.models.DownloadModel.upload_dir, verbose_name='文件')),
                ('md5sum', models.CharField(editable=False, max_length=36, null=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusinessSystem.System', verbose_name='业务系统')),
            ],
            options={
                'verbose_name': '业务软件',
                'verbose_name_plural': '业务软件',
            },
        ),
    ]
