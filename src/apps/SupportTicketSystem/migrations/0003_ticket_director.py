# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 16:51
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('SupportTicketSystem', '0002_remove_ticket_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='director',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='responsible_ticket',
                                    to='SupportTicketSystem.SupportTicketSystemUser', verbose_name='责任人'),
            preserve_default=False,
        ),
    ]
