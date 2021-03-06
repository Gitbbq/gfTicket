# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 11:18
from __future__ import unicode_literals

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('AttendanceSystem', '0009_auto_20160126_2222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-date'], 'verbose_name': '考勤记录', 'verbose_name_plural': '考勤记录'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='first_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='首次时间'),
        ),
    ]
