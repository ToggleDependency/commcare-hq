# Generated by Django 1.11.13 on 2018-06-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0051_added_zscore_grading_wfh_hfa_rec_in_month_to_agg_child_health'),
    ]

    operations = [
        migrations.CreateModel(
            name='AggregateInactiveAWW',
            fields=[
                ('awc_id', models.TextField(primary_key=True, serialize=False)),
                ('awc_name', models.TextField(blank=True, null=True)),
                ('awc_site_code', models.TextField(blank=True, null=True)),
                ('supervisor_id', models.TextField(blank=True, null=True)),
                ('supervisor_name', models.TextField(blank=True, null=True)),
                ('block_id', models.TextField(blank=True, null=True)),
                ('block_name', models.TextField(blank=True, null=True)),
                ('district_id', models.TextField(blank=True, null=True)),
                ('district_name', models.TextField(blank=True, null=True)),
                ('state_id', models.TextField(blank=True, null=True)),
                ('state_name', models.TextField(blank=True, null=True)),
                ('first_submission', models.DateField(blank=True, null=True)),
                ('last_submission', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IcdsFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blob_id', models.CharField(max_length=255)),
                ('data_type', models.CharField(max_length=255)),
                ('file_added', models.DateField(auto_now=True)),
            ],
        ),
    ]