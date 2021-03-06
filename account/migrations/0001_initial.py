# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-04 03:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='部门名称')),
                ('description', models.TextField(blank=True, null=True, verbose_name='部门介绍')),
                ('leader', models.CharField(max_length=64, verbose_name='组长')),
            ],
            options={
                'verbose_name': '部门',
                'verbose_name_plural': '部门',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='邮箱')),
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('tel', models.CharField(blank=True, max_length=11, null=True, unique=True, verbose_name='电话')),
                ('sex', models.NullBooleanField(choices=[(1, '男'), (0, '女')], verbose_name='性别')),
                ('grade', models.IntegerField(blank=True, choices=[(1, '大一'), (2, '大二'), (3, '大三'), (4, '大四')], null=True, verbose_name='年级')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Department', verbose_name='所在部门')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
