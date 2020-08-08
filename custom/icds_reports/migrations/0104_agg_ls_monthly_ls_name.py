# Generated by Django 1.11.16 on 2019-03-12 10:52
from corehq.sql_db.operations import RawSQLMigration
from django.db import migrations

from custom.icds_reports.const import SQL_TEMPLATES_ROOT

migrator = RawSQLMigration((SQL_TEMPLATES_ROOT,))


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0103_aggregateccsrecordcomplementaryfeedingforms_supervisor_id'),
    ]

    operations = [
        migrator.get_migration('update_tables44.sql'),
    ]