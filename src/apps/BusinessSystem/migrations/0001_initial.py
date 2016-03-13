# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 22:34
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(default=0.0, verbose_name='顺位')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('url', models.URLField(blank=True, null=True, verbose_name='网址')),
                ('bs', models.BooleanField(default=False, verbose_name='B/S系统')),
                ('cs', models.BooleanField(default=False, verbose_name='C/S系统')),
                ('developer', models.CharField(choices=[('zoh', '总行'), ('bej', '北京分行'), ('YJH', '银监'), ('RH', '人行'), ('third', '第三方')], max_length=127, verbose_name='开发商')),
            ],
            options={
                'verbose_name': '系统',
                'verbose_name_plural': '系统',
            },
        ),
    ]
