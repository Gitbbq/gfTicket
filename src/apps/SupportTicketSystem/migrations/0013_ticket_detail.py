# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SupportTicketSystem', '0012_auto_20160219_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='detail',
            field=models.TextField(blank=True, null=True, verbose_name='详细信息'),
        ),
    ]
