# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('DownloadCenter', '0010_businesssoftware'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesssoftware',
            name='manual',
            field=models.TextField(blank=True, null=True, verbose_name='说明'),
        ),
    ]