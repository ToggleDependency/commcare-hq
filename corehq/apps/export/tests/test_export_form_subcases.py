import json
import os
from mock import patch

from django.test import TestCase

from couchexport.models import Format

from corehq.util.context_managers import drop_connected_signals
from corehq.apps.app_manager.tests.util import TestXmlMixin
from corehq.apps.app_manager.models import XForm, Application
from corehq.apps.app_manager.signals import app_post_save
from corehq.apps.export.dbaccessors import delete_all_export_data_schemas
from corehq.apps.export.models import FormExportDataSchema, FormExportInstance
from corehq.apps.export.export import get_export_file


class TestFormExportSubcases(TestCase, TestXmlMixin):
    """
    These tests operate on an MCH app which uses various means of creating cases.
    We care most about module 0 ("Mothers") > form 1 ("Followup Form")
    The primary case type is "mom" - this form updates mom cases, but doesn't create them
    This form creates a single "voucher" case using the normal case management interface
        case_name is set to /data/voucher-name
    This form creates "baby" cases in a repeat group also using the normal case management interface
        case_name is set to /data/babies/whats_the_babys_name
    A "prescription" case can also be created using save-to-case.
        case_name is /data/prescription/prescription_name
        the save-to-case node is /data/prescription/prescription
    """
    file_path = ['data']
    root = os.path.dirname(__file__)
    domain = 'app_with_subcases'
    app_json_file = 'app_with_subcases'
    form_xml_file = 'app_with_subcases_form'
    form_es_response_file = 'app_with_subcases_submission'
    form_xmlns = "http://openrosa.org/formdesigner/EA845CA3-4B57-47C4-AFF4-5884E40228D7"

    @classmethod
    def setUpClass(cls):
        super(TestFormExportSubcases, cls).setUpClass()
        cls.app = Application.wrap(cls.get_json(cls.app_json_file))
        cls.xform = XForm(cls.get_xml(cls.form_xml_file))
        cls.form_es_response = cls.get_json(cls.form_es_response_file)
        with drop_connected_signals(app_post_save):
            cls.app.save()

    @classmethod
    def tearDownClass(cls):
        cls.app.delete()
        delete_all_export_data_schemas()
        super(TestFormExportSubcases, cls).tearDownClass()

    def assertContainsPaths(self, paths, export_group_schema):
        """
        paths should be of the form ["form.question1", "form.group.question2"]
        """
        actual_paths = {
            ".".join(node.name for node in item.path)
            for item in export_group_schema.items
        }
        missing = set(paths) - actual_paths
        if missing:
            raise AssertionError("Contains paths:\n  {}\nMissing paths:\n  {}"
                                 .format('\n  '.join(actual_paths), '\n  '.join(missing)))

    def test(self):
        with patch('corehq.apps.app_manager.models.FormBase.wrapped_xform', lambda _: self.xform):
            schema = FormExportDataSchema.generate_schema_from_builds(
                self.domain,
                self.app._id,
                self.form_xmlns,
                only_process_current_builds=True,
            )

        for group_schema in schema.group_schemas:
            # group_schema is an instance of ExportGroupSchem
            # group_schema.items is an array of ExportItems subclasses
            path = [node.name for node in group_schema.path]
            if path == []:
                main_group_schema = group_schema
            elif path == ['form', 'babies']:
                baby_repeat_group_schema = group_schema
            elif path == ['form', 'subcase_0']:
                voucher_subcase_schema = group_schema

        self.assertContainsPaths(
            [
                # Verify that a simple form question appears in the schema
                'form.how_are_you_today',

                # Verify that the main parent case updates appear (case type "mom")
                'form.case.update.last_status',
            ],
            main_group_schema
        )

        # Verify that we see updates from subcases in repeat groups (case type "baby")
        self.assertContainsPaths(
            [
                'form.babies.case.@case_id',
                'form.babies.case.@date_modified',
                'form.babies.case.@user_id',
                'form.babies.case.create.case_name',
                'form.babies.case.create.case_type',
                'form.babies.case.create.owner_id',
                'form.babies.case.update.eye_color',
            ],
            baby_repeat_group_schema
        )

        # Verify that we see updates from subcases not in repeat groups (case type "voucher")
        self.assertContainsPaths(
            [
                'form.subcase_0.case.@case_id',
                'form.subcase_0.case.@date_modified',
                'form.subcase_0.case.@user_id',
                'form.subcase_0.case.create.case_name',
                'form.subcase_0.case.create.case_type',
                'form.subcase_0.case.create.owner_id',
                'form.subcase_0.case.update.how_many_babies',
            ],
            voucher_subcase_schema,
        )

        instance = FormExportInstance.generate_instance_from_schema(schema)
        instance.export_format = Format.JSON
        # make everything show up in the export
        for table in instance.tables:
            table.selected = True
            for column in table.columns:
                column.selected = True

        with patch('corehq.apps.export.export._get_export_documents') as docs:
            docs.return_value = self.form_es_response
            export_file = get_export_file([instance], [])

        with export_file as export:
            export_data = json.loads(export.read())

        def get_form_data(table):
            headers = export_data[table]['headers']
            return [
                dict(zip(headers, row))
                for row in export_data[table]['rows']
            ]

        self.assertDictContainsSubset({
            # I don't know what these ones are - normal form case?
            # (This is a followup, not registration form)
            "create.case_name": "---",
            "create.case_type": "---",
            "create.owner_id": "---",

            # normal form questions
            "form.add_a_prescription": "yes",
            "form.how_are_you_today": "fine_thanks",
            "form.how_many_babies": "2",
            "form.is_this_a_delivery": "yes",
            "form.voucher-name": "Petunia2017-08-28",

            # standard case update
            "form.case.update.last_status": "fine_thanks",

            # save-to-case properties
            "form.prescription.prescription.case.create.case_name": "Petunia-prescription-2017-08-28",
            "form.prescription.prescription.case.create.case_type": "prescription",
            "form.prescription.prescription.case.update.number_of_babies": "2",
            "form.prescription.prescription_name": "Petunia-prescription-2017-08-28"
        }, get_form_data('Forms')[0])

        self.assertDictContainsSubset({
            "form.babies.eye_color": "blue",
            "form.babies.whats_the_babys_name": "Bob",

            "form.babies.case.@case_id": "601b6d19-db70-4878-8b93-aeeb99982d3f",
            "form.babies.case.@date_modified": "2017-08-28 20:21:28",
            "form.babies.case.@user_id": "853a24735ba89a3019ced7e3153dc60d",

            "form.babies.case.create.case_name": "Bob",
            "form.babies.case.create.case_type": "baby",
            "form.babies.case.create.owner_id": "853a24735ba89a3019ced7e3153dc60d",

            "form.babies.case.update.eye_color": "blue",
        }, get_form_data('Repeat- babies')[0])
