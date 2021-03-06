# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 15:38
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('IPAddress', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='description',
            field=models.TextField(default='None', max_length=255, verbose_name='详细描述'),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(default='None', max_length=255, verbose_name='主机名'),
        ),
        migrations.AlterField(
            model_name='host',
            name='subnet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosts', to='IPAddress.Subnet', verbose_name='子网'),
        ),
        migrations.AlterField(
            model_name='subnet',
            name='description',
            field=models.TextField(blank=True, default='None', max_length=255, verbose_name='详细描述'),
        ),
        migrations.AlterField(
            model_name='subnet',
            name='summary',
            field=models.CharField(default='None', max_length=128, verbose_name='简介'),
        ),
    ]
