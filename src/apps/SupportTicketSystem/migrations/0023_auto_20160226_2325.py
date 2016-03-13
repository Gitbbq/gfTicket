# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 23:25
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SupportTicketSystem', '0022_auto_20160226_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='responsible_person',
            field=models.ForeignKey(blank=True, help_text='一般事件留空即可，会自动根据区域安排', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responsible_ticket',
                                    to='SupportTicketSystem.SupportTicketSystemUser', verbose_name='责任人'),
        ),
    ]