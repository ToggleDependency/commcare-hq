# Generated by Django 1.11.16 on 2018-11-07 16:51
from corehq.sql_db.operations import RawSQLMigration
from django.db import migrations, models

from custom.icds_reports.const import SQL_TEMPLATES_ROOT

migrator = RawSQLMigration((SQL_TEMPLATES_ROOT,))


class Migration(migrations.Migration):

    dependencies = [
        ('icds_reports', '0073_ccsrecordmonthly_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awwincentivereport',
            name='expected_visits',
            field=models.DecimalField(decimal_places=2, max_digits=64, null=True),
        ),
        migrator.get_migration('update_tables30.sql'),
    ]