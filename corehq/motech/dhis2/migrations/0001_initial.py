# Generated by Django 1.9.12 on 2017-03-16 15:41

from django.db import migrations, models

import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JsonApiLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=126)),
                ('timestamp', models.DateTimeField()),
                ('request_method', models.CharField(max_length=12)),
                ('request_url', models.CharField(max_length=255)),
                ('request_headers', jsonfield.fields.JSONField(blank=True)),
                ('request_params', jsonfield.fields.JSONField(blank=True)),
                ('request_body', jsonfield.fields.JSONField(blank=True)),
                ('request_error', models.TextField(blank=True)),
                ('response_status', models.IntegerField()),
                ('response_body', models.TextField(blank=True)),
            ],
        ),
    ]
