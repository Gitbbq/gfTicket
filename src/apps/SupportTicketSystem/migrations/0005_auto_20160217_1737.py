# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 17:37
from __future__ import unicode_literals

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SupportTicketSystem', '0004_auto_20160217_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='是否已完成'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='completed_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='completed_ticket',
                                    to='SupportTicketSystem.SupportTicketSystemUser', verbose_name='完成人'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='completed_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='完成事件'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='scheduled_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 2, 17, 17, 37, 38, 524564), verbose_name='预计完成时间'),
            preserve_default=False,
        ),
    ]
