# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=100, verbose_name='主机名')),
                ('os', models.CharField(max_length=100, verbose_name='操作系统')),
                ('public_ip', models.CharField(max_length=100, verbose_name='公网IP')),
                ('intranet_ip', models.CharField(max_length=100, verbose_name='内网IP')),
                ('cpu_num', models.CharField(max_length=100, verbose_name='CPU型号')),
                ('memory_size', models.CharField(max_length=50, verbose_name='内存')),
                ('disk_size', models.CharField(max_length=50, verbose_name='磁盘')),
                ('installed_software', models.CharField(max_length=100, verbose_name='已安装软件')),
            ],
            options={
                'verbose_name_plural': '服务器列表',
            },
        ),
    ]
