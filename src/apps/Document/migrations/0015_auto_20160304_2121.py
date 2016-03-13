# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 21:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Document', '0014_auto_20160304_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='relevant_system',
        ),
        migrations.AlterField(
            model_name='documentuser',
            name='permission',
            field=models.IntegerField(choices=[(0, '访客'), (1, '一般权限'), (2, '高级权限')], default=0, verbose_name='拥有权限'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='require_permission',
            field=models.IntegerField(choices=[(0, '访客'), (1, '一般权限'), (2, '高级权限')], default=0, verbose_name='所需权限'),
        ),
    ]
