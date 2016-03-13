# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('BranchManager', '0004_auto_20160218_0035'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='db_active',
            field=models.BooleanField(default=True, verbose_name='激活'),
        ),
        migrations.AddField(
            model_name='department',
            name='db_active',
            field=models.BooleanField(default=True, verbose_name='激活'),
        ),
        migrations.AddField(
            model_name='departmenttype',
            name='db_active',
            field=models.BooleanField(default=True, verbose_name='激活'),
        ),
        migrations.AddField(
            model_name='subdepartment',
            name='db_active',
            field=models.BooleanField(default=True, verbose_name='激活'),
        ),
    ]
