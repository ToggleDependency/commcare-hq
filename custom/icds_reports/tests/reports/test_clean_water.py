from __future__ import absolute_import
from django.test.utils import override_settings

from custom.icds_reports.const import ChartColors
from custom.icds_reports.reports.clean_water import get_clean_water_data_map, get_clean_water_data_chart, \
    get_clean_water_sector_data
from django.test import TestCase


@override_settings(SERVER_ENVIRONMENT='icds')
class TestCleanWater(TestCase):

    def test_map_data(self):
        self.assertDictEqual(
            get_clean_water_data_map(
                'icds-cas',
                config={
                    'month': (2017, 5, 1),
                    'aggregation_level': 5
                },
                loc_level='state'
            )[0],
            {
                "rightLegend": {
                    "info": "Percentage of AWCs that reported having a source of clean drinking water",
                    "average": 145.0
                },
                "fills": {
                    "0%-25%": "#de2d26",
                    "25%-75%": "#fc9272",
                    "75%-100%": "#fee0d2",
                    "defaultFill": "#9D9D9D"
                },
                "data": {
                    "st1": {
                        "in_month": 17,
                        "all": 9,
                        "fillKey": "75%-100%"
                    },
                    "st2": {
                        "in_month": 12,
                        "all": 11,
                        "fillKey": "75%-100%"
                    }
                },
                "slug": "clean_water",
                "label": "Percentage of AWCs that reported having a source of clean drinking water"
            }
        )

    def test_chart_data(self):
        self.assertDictEqual(
            get_clean_water_data_chart(
                'icds-cas',
                config={
                    'month': (2017, 5, 1),
                    'aggregation_level': 5
                },
                loc_level='state'
            ),
            {
                "location_type": "State",
                "bottom_five": [
                    {
                        "loc_name": "st1",
                        "percent": 188.88888888888889
                    },
                    {
                        "loc_name": "st2",
                        "percent": 109.0909090909091
                    }
                ],
                "top_five": [
                    {
                        "loc_name": "st1",
                        "percent": 188.88888888888889
                    },
                    {
                        "loc_name": "st2",
                        "percent": 109.0909090909091
                    }
                ],
                "chart_data": [
                    {
                        "color": ChartColors.BLUE,
                        "classed": "dashed",
                        "strokeWidth": 2,
                        "values": [
                            {
                                "y": 0.0,
                                "x": 1485907200000,
                                "in_month": 0
                            },
                            {
                                "y": 0.0,
                                "x": 1488326400000,
                                "in_month": 0
                            },
                            {
                                "y": 0.3888888888888889,
                                "x": 1491004800000,
                                "in_month": 14
                            },
                            {
                                "y": 1.45,
                                "x": 1493596800000,
                                "in_month": 29
                            }
                        ],
                        "key": "Percentage of AWCs that reported having a source of clean drinking water"
                    }
                ],
                "all_locations": [
                    {
                        "loc_name": "st1",
                        "percent": 188.88888888888889
                    },
                    {
                        "loc_name": "st2",
                        "percent": 109.0909090909091
                    }
                ]
            }
        )

    def test_sector_data(self):
        self.assertDictEqual(
            get_clean_water_sector_data(
                'icds-cas',
                config={
                    'month': (2017, 5, 1),
                    'state_id': 'st1',
                    'district_id': 'd1',
                    'block_id': 'b1',
                    'aggregation_level': 5
                },
                location_id='b1',
                loc_level='supervisor'
            ),
            {
                "info": "Percentage of AWCs that reported having a source of clean drinking water",
                "tooltips_data": {
                    "s2": {
                        "in_month": 3,
                        "all": 4
                    },
                    "s1": {
                        "in_month": 5,
                        "all": 2
                    }
                },
                "chart_data": [
                    {
                        "color": "#006fdf",
                        "classed": "dashed",
                        "strokeWidth": 2,
                        "values": [
                            [
                                "s1",
                                2.5
                            ],
                            [
                                "s2",
                                0.75
                            ]
                        ],
                        "key": ""
                    }
                ]
            }
        )
