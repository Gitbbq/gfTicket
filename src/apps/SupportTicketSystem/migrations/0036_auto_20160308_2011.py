# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-08 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupportTicketSystem', '0035_ticket_wait_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='wait_admin',
        ),
        migrations.AddField(
            model_name='ticket',
            name='push_to_admin',
            field=models.BooleanField(default=False, verbose_name='提交给管理员'),
        ),
    ]
