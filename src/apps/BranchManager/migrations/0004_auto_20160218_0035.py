# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('BranchManager', '0003_auto_20160215_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='db_manual_order',
            field=models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位'),
        ),
        migrations.AlterField(
            model_name='department',
            name='db_manual_order',
            field=models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位'),
        ),
        migrations.AlterField(
            model_name='departmenttype',
            name='db_manual_order',
            field=models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位'),
        ),
        migrations.AlterField(
            model_name='subdepartment',
            name='db_manual_order',
            field=models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位'),
        ),
    ]
