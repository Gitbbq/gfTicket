# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 19:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPAddress', '0018_remove_host_ping_last_success_fraction_loss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='ping_last_success_delay',
        ),
    ]
