# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('BranchManager', '0003_auto_20160215_1639'),
        ('SupportTicketSystem', '0003_ticket_director'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='director',
            new_name='responsible_person',
        ),
        migrations.AddField(
            model_name='supportticketsystemuser',
            name='precinct',
            field=models.ManyToManyField(blank=True, related_name='responsible_person', to='BranchManager.Area', verbose_name='管辖区域'),
        ),
    ]
