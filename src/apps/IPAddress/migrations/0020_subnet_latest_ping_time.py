# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 20:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IPAddress', '0019_remove_host_ping_last_success_delay'),
    ]

    operations = [
        migrations.AddField(
            model_name='subnet',
            name='latest_ping_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='最后Ping时间'),
        ),
    ]
