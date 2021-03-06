# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 12:00
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sso', '0002_auto_20160124_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADServer',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('sso.domainsetting',),
        ),
        migrations.RemoveField(
            model_name='domainuser',
            name='objectSid',
        ),
        migrations.AddField(
            model_name='domainuser',
            name='domain',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sso.DomainSetting', verbose_name='域'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='domainuser',
            name='username',
            field=models.CharField(default=1, max_length=642, verbose_name='username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='domainuser',
            name='cn',
            field=models.CharField(blank=True, max_length=642, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='domainuser',
            name='displayName',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Display Name'),
        ),
    ]
