# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SupportTicketSystem', '0008_auto_20160218_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trouble',
            name='for_short',
            field=models.CharField(max_length=24, verbose_name='缩写'),
        ),
    ]