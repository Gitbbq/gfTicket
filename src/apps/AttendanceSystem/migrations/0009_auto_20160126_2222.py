# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-26 22:22
from __future__ import unicode_literals

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('AttendanceSystem', '0008_auto_20160126_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='first_time',
            field=models.TimeField(default=datetime.datetime(2016, 1, 26, 22, 22, 45, 103342), verbose_name='首次时间'),
        ),
    ]
