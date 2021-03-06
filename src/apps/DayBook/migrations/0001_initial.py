# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 11:49
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('BranchManager', '0008_auto_20160324_2256'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DayBookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位')),
                ('db_active', models.BooleanField(db_index=True, default=True, verbose_name='激活')),
                ('internet_pc_add', models.BooleanField(default=False, verbose_name='添加外网机')),
                ('internet_pc_edit', models.BooleanField(default=False, verbose_name='修改外网机')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='daybook_user', to=settings.AUTH_USER_MODEL, verbose_name='对应用户')),
            ],
            options={
                'verbose_name': '台帐用户',
                'verbose_name_plural': '台帐用户',
            },
        ),
        migrations.CreateModel(
            name='InternetPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位')),
                ('db_active', models.BooleanField(db_index=True, default=True, verbose_name='激活')),
                ('case_sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='主机序列号')),
                ('screen_sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='显示器序列号')),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP地址')),
                ('hostname', models.CharField(blank=True, max_length=128, null=True, verbose_name='主机名')),
                ('description', models.TextField(blank=True, null=True, verbose_name='详细描述')),
                ('history', django.contrib.postgres.fields.jsonb.JSONField(default={'log': []}, editable=False, verbose_name='历史')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='internet_pc', to='BranchManager.Department', verbose_name='网点')),
            ],
            options={
                'verbose_name': '外网机',
                'verbose_name_plural': '外网机',
                'ordering': ['-db_manual_order', '-db_modified'],
            },
        ),
    ]
