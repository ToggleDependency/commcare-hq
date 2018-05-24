# coding=utf-8
from __future__ import absolute_import
from __future__ import unicode_literals
from mock.mock import MagicMock

from custom.intrahealth.tests.utils import YeksiTestCase
from custom.intrahealth.reports import Dashboard3Report


class TestDashboard3(YeksiTestCase):

    def test_satisfaction_rate_after_delivery_data_report(self):
        mock = MagicMock()
        mock.couch_user = self.user
        mock.GET = {
            'location_id': '',
            'program': '',
            'month_start': '10',
            'year_start': '2017',
            'month_end': '3',
            'year_end': '2018',
        }

        dashboard3_report = Dashboard3Report(request=mock, domain='test-pna')

        satisfaction_rate_after_delivery_data_report = \
            dashboard3_report.report_context['reports'][0]['report_table']
        headers = satisfaction_rate_after_delivery_data_report['headers'].as_export_table[0]
        rows = satisfaction_rate_after_delivery_data_report['rows']
        total_row = satisfaction_rate_after_delivery_data_report['total_row']

        self.assertEqual(
            headers,
            ['Produit', 'Octobre 2017', 'Novembre 2017', 'Décembre 2017', 'Janvier 2018',
             'Février 2018', 'Mars 2018']
        )
        self.assertEqual(
            rows,
            sorted([
                [
                    'ACETATE DE MEDROXY PROGESTERONE 104MG/0.65ML INJ. (SAYANA PRESS)',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'ACETATE DE MEDROXY PROGESTERONE 150MG/ML+S A B KIT (1+1) (DEPO-PROVERA)',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': 'color: orange', 'html': '150.00%'}
                ],
                [
                    'ACT ADULTE',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'ACT PETIT ENFANT',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'ALBENDAZOL 4% SB.',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'DISPOSITIF INTRA UTERIN (TCU 380 A) - DIU',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': 'color: orange', 'html': '1462.40%'}
                ],
                [
                    'EFAVIRENZ 600MG CP.',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': 'color: red', 'html': '80.77%'}
                ],
                [
                    'LAMIVUDINE+NEVIRAPINE+ZIDOVUDINE (30+50+60)MG CP.',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'LEVONORGESTREL+ETHYNILESTRADIOL+FER (0.15+0.03+75)MG (MICROGYNON)',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': 'color: orange', 'html': '222.22%'}
                ],
                [
                    'NEVIRAPINE 200MG CP.',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '93.30%'}
                ],
                [
                    'PARACETAMOL 500MG CP.',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'}
                ],
                [
                    'Produit 1',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'}
                ],
                [
                    'Produit 10',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': 'color: red', 'html': '87.10%'},
                    {'style': '', 'html': '96.30%'}
                ],
                [
                    'Produit 12',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'}
                ],
                [
                    'Produit 14',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '90.00%'}
                ],
                [
                    'Produit 15',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'Produit 2',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'Produit A',
                    {'style': '', 'html': '97.63%'},
                    {'style': '', 'html': '94.86%'},
                    {'style': '', 'html': '100.00%'},
                    {'style': '', 'html': '100.00%'},
                    {'style': '', 'html': '95.24%'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'Produit B',
                    {'style': '', 'html': '98.28%'},
                    {'style': '', 'html': '98.94%'},
                    {'style': '', 'html': '98.60%'},
                    {'style': 'color: orange', 'html': '142.86%'},
                    {'style': 'color: orange', 'html': '166.67%'},
                    {'style': 'color: orange', 'html': '114.29%'}
                ],
                [
                    'Produit C',
                    {'style': '', 'html': '93.88%'},
                    {'style': '', 'html': '93.28%'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': 'color: orange', 'html': '111.11%'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'}
                ],
                [
                    'RIFAMPICINE+ISONIAZIDE (150+75)MG CP.',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': 'color: orange', 'html': '101.21%'}
                ],
                [
                    'RIFAMPICINE+ISONIAZIDE+PYRAZINAMIDE (60+30+150)MG CP. DISPER',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'RIFAMPICINE+ISONIAZIDE+PYRAZINAMIDE+ETHAMBUTOL (150+75+400+2',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ],
                [
                    'TEST RAPIDE HIV 1/2 (SD BIOLINE)',
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': 'pas de donn\xe9es'},
                    {'style': '', 'html': '100.00%'}
                ]
            ], key=lambda x: x[0])
        )
        self.assertEqual(
            total_row,
            [
                'Total (CFA)',
                {'style': '', 'html': '96.89%'},
                {'style': '', 'html': '95.77%'},
                {'style': '', 'html': '99.02%'},
                {'style': 'color: orange', 'html': '119.05%'},
                {'style': 'color: orange', 'html': '114.47%'},
                {'style': 'color: orange', 'html': '188.23%'}
            ]

        )

    def test_valuation_of_pna_stock_per_product_data_report(self):
        mock = MagicMock()
        mock.couch_user = self.user
        mock.GET = {
            'location_id': '',
            'program': '',
            'month_start': '10',
            'year_start': '2017',
            'month_end': '3',
            'year_end': '2018',
        }

        dashboard3_report = Dashboard3Report(request=mock, domain='test-pna')

        valuation_of_pna_stock_per_product_data_report = \
            dashboard3_report.report_context['reports'][1]['report_table']
        headers = valuation_of_pna_stock_per_product_data_report['headers'].as_export_table[0]
        rows = valuation_of_pna_stock_per_product_data_report['rows']
        total_row = valuation_of_pna_stock_per_product_data_report['total_row']

        self.assertEqual(
            headers,
            ['Produit', 'Octobre 2017', 'Novembre 2017', 'Décembre 2017', 'Janvier 2018',
             'Février 2018', 'Mars 2018']
        )
        self.assertItemsEqual(
            rows,
            sorted([
                ['ACETATE DE MEDROXY PROGESTERONE 104MG/0.65ML INJ. (SAYANA PRESS)', '0.00', '0.00', '0.00',
                 '0.00', '0.00', '0.00'],
                ['ACETATE DE MEDROXY PROGESTERONE 150MG/ML+S A B KIT (1+1) (DEPO-PROVERA)', '0.00', '0.00',
                 '0.00', '0.00', '0.00', '0.00'],
                ['ACT ADULTE', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['ACT PETIT ENFANT', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['ALBENDAZOL 4% SB.', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['DISPOSITIF INTRA UTERIN (TCU 380 A) - DIU', '0.00', '0.00', '0.00', '0.00', '0.00',
                 '0.00'], ['EFAVIRENZ 600MG CP.', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['LAMIVUDINE+NEVIRAPINE+ZIDOVUDINE (30+50+60)MG CP.', '0.00', '0.00', '0.00', '0.00', '0.00',
                 '0.00'],
                ['LEVONORGESTREL+ETHYNILESTRADIOL+FER (0.15+0.03+75)MG (MICROGYNON)', '0.00', '0.00', '0.00',
                 '0.00', '0.00', '0.00'],
                ['NEVIRAPINE 200MG CP.', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['PARACETAMOL 500MG CP.', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['Produit 1', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['Produit 10', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['Produit 12', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['Produit 14', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['Produit 15', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['Produit 2', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['Produit A', '442500.00', '717500.00', '412500.00', '150000.00', '437500.00', '150000.00'],
                ['Produit B', '336000.00', '558000.00', '334500.00', '157500.00', '453000.00', '127500.00'],
                ['Produit C', '198000.00', '386400.00', '0.00', '120000.00', '0.00', '0.00'],
                ['RIFAMPICINE+ISONIAZIDE (150+75)MG CP.', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00'],
                ['RIFAMPICINE+ISONIAZIDE+PYRAZINAMIDE (60+30+150)MG CP. DISPER', '0.00', '0.00', '0.00',
                 '0.00', '0.00', '0.00'],
                ['RIFAMPICINE+ISONIAZIDE+PYRAZINAMIDE+ETHAMBUTOL (150+75+400+2', '0.00', '0.00', '0.00',
                 '0.00', '0.00', '0.00'],
                ['TEST RAPIDE HIV 1/2 (SD BIOLINE)', '0.00', '0.00', '0.00', '0.00', '0.00', '0.00']
            ], key=lambda x: x[0])
        )
        self.assertEqual(
            total_row,
            [
                'Total (CFA)', '976500.00', '1661900.00', '747000.00', '427500.00', '890500.00',
                '277500.00'
            ]
        )
