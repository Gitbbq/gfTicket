# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-07 21:32
from __future__ import unicode_literals

import apps.Core.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('SupportTicketSystem', '0029_projectevent_completed_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectEventFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位')),
                ('db_active', models.BooleanField(db_index=True, default=True, verbose_name='激活')),
                ('filename', models.CharField(editable=False, max_length=255, null=True, verbose_name='文件名')),
                ('content_type', models.CharField(editable=False, max_length=127, null=True, verbose_name='Content Type')),
                ('orig_file', models.FileField(help_text='选择一个文件并上传', upload_to=apps.Core.models.DownloadModel.upload_dir, verbose_name='文件')),
                ('md5sum', models.CharField(editable=False, max_length=36, null=True)),
                ('manual', models.TextField(blank=True, null=True, verbose_name='说明')),
                ('project_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='SupportTicketSystem.ProjectEvent')),
            ],
            options={
                'verbose_name_plural': '项目事件附件',
                'verbose_name': '项目事件附件',
            },
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位')),
                ('db_active', models.BooleanField(db_index=True, default=True, verbose_name='激活')),
                ('filename', models.CharField(editable=False, max_length=255, null=True, verbose_name='文件名')),
                ('content_type', models.CharField(editable=False, max_length=127, null=True, verbose_name='Content Type')),
                ('orig_file', models.FileField(help_text='选择一个文件并上传', upload_to=apps.Core.models.DownloadModel.upload_dir, verbose_name='文件')),
                ('md5sum', models.CharField(editable=False, max_length=36, null=True)),
                ('manual', models.TextField(blank=True, null=True, verbose_name='说明')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='SupportTicketSystem.Project')),
            ],
            options={
                'verbose_name_plural': '项目附件',
                'verbose_name': '项目附件',
            },
        ),
        migrations.CreateModel(
            name='TicketFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, db_index=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(db_index=True, default=0.0, editable=False, verbose_name='顺位')),
                ('db_active', models.BooleanField(db_index=True, default=True, verbose_name='激活')),
                ('filename', models.CharField(editable=False, max_length=255, null=True, verbose_name='文件名')),
                ('content_type', models.CharField(editable=False, max_length=127, null=True, verbose_name='Content Type')),
                ('orig_file', models.FileField(help_text='选择一个文件并上传', upload_to=apps.Core.models.DownloadModel.upload_dir, verbose_name='文件')),
                ('md5sum', models.CharField(editable=False, max_length=36, null=True)),
                ('manual', models.TextField(blank=True, null=True, verbose_name='说明')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='SupportTicketSystem.Ticket')),
            ],
            options={
                'verbose_name_plural': '日常事件附件',
                'verbose_name': '日常事件附件',
            },
        ),
    ]
