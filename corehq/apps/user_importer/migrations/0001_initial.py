# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-07 02:58
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserUploadRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=256)),
                ('result', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('task_id', models.CharField(max_length=40)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.CharField(max_length=40)),
            ],
        ),
    ]