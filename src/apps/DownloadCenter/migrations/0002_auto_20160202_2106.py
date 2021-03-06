# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 21:06
from __future__ import unicode_literals

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Equipment', '0001_initial'),
        ('DownloadCenter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_created', models.DateTimeField(auto_now_add=True, verbose_name='创建日期')),
                ('db_modified', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('db_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('db_manual_order', models.FloatField(default=0.0, verbose_name='顺位')),
                ('filename', models.CharField(editable=False, max_length=255, null=True, verbose_name='文件名')),
                ('content_type', models.CharField(editable=False, max_length=127, null=True, verbose_name='Content Type')),
                ('orig_file', models.FileField(help_text='选择一个文件并上传', upload_to='attachment/492f3c09-cadc-465a-8dad-343f31fc60b1/', verbose_name='文件')),
                ('md5sum', models.CharField(editable=False, max_length=36, null=True)),
                ('os_compatibility', models.CharField(choices=[('32', '32位'), ('64', '64位'), ('all', '通用')], max_length=127, verbose_name='兼容性')),
                ('equipment_model', models.ManyToManyField(to='Equipment.EquipmentModel', verbose_name='适配设备型号')),
            ],
            options={
                'verbose_name': '驱动程序',
                'verbose_name_plural': '驱动程序',
            },
        ),
        migrations.AlterField(
            model_name='attachment',
            name='orig_file',
            field=models.FileField(help_text='选择一个文件并上传', upload_to='attachment/445f09ff-08d8-4643-a8f8-e13d81b52e48/', verbose_name='文件'),
        ),
    ]
