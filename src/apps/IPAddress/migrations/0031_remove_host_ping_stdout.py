# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-18 20:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IPAddress', '0030_host_ping_stdout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='ping_stdout',
        ),
    ]