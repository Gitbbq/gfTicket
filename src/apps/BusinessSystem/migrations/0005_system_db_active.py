# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('BusinessSystem', '0004_system_for_short'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='db_active',
            field=models.BooleanField(default=True, verbose_name='激活'),
        ),
    ]
