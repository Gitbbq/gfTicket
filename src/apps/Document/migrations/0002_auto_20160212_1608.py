# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Document', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='type',
            field=models.CharField(choices=[('system ', '系统配置手册'), ('debug', '排错'), ('page', '页面')], default='blog', max_length=255, verbose_name='类型'),
        ),
    ]
