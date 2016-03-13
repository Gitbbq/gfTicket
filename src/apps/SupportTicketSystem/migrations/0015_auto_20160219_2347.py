# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 23:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SupportTicketSystem', '0014_auto_20160219_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='contact',
        ),
        migrations.AddField(
            model_name='ticket',
            name='contact_name',
            field=models.CharField(default=' ', max_length=127, verbose_name='联系人'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='contact_telephone',
            field=models.CharField(default=' ', max_length=127, verbose_name='电话'),
        ),
    ]
