# Generated by Django 1.11.16 on 2019-03-12 10:52
from corehq.sql_db.operations import RawSQLMigration
from django.db import migrations

from custom.icds_reports.const import SQL_TEMPLATES_ROOT

migrator = RawSQLMigration((SQL_TEMPLATES_ROOT, 'database_views'))


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0105_aww_incentive_report_monthly'),
    ]

    operations = [
        migrator.get_migration('service_delivery_monthly.sql'),
    ]