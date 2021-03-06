# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-04 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Document', '0013_auto_20160304_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentuser',
            name='advanced_permission',
        ),
        migrations.RemoveField(
            model_name='documentuser',
            name='generic_permission',
        ),
        migrations.AddField(
            model_name='documentuser',
            name='permission',
            field=models.IntegerField(choices=[(0, '访客可访问'), (1, '一般权限'), (2, '需要高级权限')], default=0, verbose_name='拥有权限'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='require_permission',
            field=models.IntegerField(choices=[(0, '访客可访问'), (1, '一般权限'), (2, '需要高级权限')], default=0, verbose_name='所需权限'),
        ),
    ]
