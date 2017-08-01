from floodviz.reference_parser import parse_reference_data
from floodviz import reference_parser

import unittest
from unittest import mock
import builtins

class TestReferenceParser(unittest.TestCase):

    def setUp(self):

        self.mock_reference = {"target_epsg": "EPSG:2794",
                               "site_ids": ["05463500", "05471050", "05420680", "05479000", "05484000", "05481000", "05486000", "05421000",
                                            "05485500", "05455100", "05470500", "05451500", "05458000", "05471000", "05462000", "05457700", "05458500",
                                            "05470000", "05484500", "05481300", "05464220", "05458900", "05485605", "05463000", "05471200", "05476750",
                                            "05411850", "05454220", "05481950", "05416900", "05464500", "05487470"],
                               "display_sites": ["05471200", "05476750", "05411850", "05462000"],
                               "bbox": [-95.3, 39.8, -91, 43.6],
                               "startDate": "2008-06-05",
                               "endDate": "2008-06-15",
                               "peak": {
                                   "site": "05462000",
                                   "dv_date": "2008-06-09"
                               },
                               "reference": {
                                   "type": "FeatureCollection",
                                   "crs": {
                                       "type": "name",
                                       "properties": {
                                           "name": "urn:ogc:def:crs:OGC:1.3:CRS84"
                                       }
                                   },
                                   "features": [
                                       {
                                           "type": "Feature",
                                           "id": 0,
                                           "properties": {
                                               "gnis_id": " ",
                                               "gnis_name": " ",
                                               "reftype": "rivers"
                                           },
                                           "geometry": {
                                               "type": "MultiLineString",
                                               "coordinates": []
                                           }
                                       },
                                       {
                                           "type": "Feature",
                                           "geometry": {
                                               "type": "Point",
                                               "coordinates": [
                                               ]
                                           },
                                           "properties": {
                                               "name": "Cedar Rapids IA",
                                               "country.etc": "IA",
                                               "pop": "123243",
                                               "capital": "0",
                                               "reftype": "city"
                                           }
                                       },
                                       {
                                           "type": "Feature",
                                           "geometry": {
                                               "type": "Polygon",
                                               "coordinates": []
                                           },
                                           "properties": {
                                               "group": "12",
                                               "order": " 2951",
                                               "region": "illinois",
                                               "reftype": "politicalBoundaries"
                                           }
                                       }
                                   ]
                               }
                               }


        self.mock_response = {'epsg': '2794', 'site_ids': ['05463500', '05471050', '05420680', '05479000', '05484000', '05481000', '05486000', '05421000', '05485500', '05455100', '05470500', '05451500', '05458000', '05471000', '05462000', '05457700', '05458500', '05470000', '05484500', '05481300', '05464220', '05458900', '05485605', '05463000', '05471200', '05476750', '05411850', '05454220', '05481950', '05416900', '05464500', '05487470'], 'display_sites': ['05471200', '05476750', '05411850', '05462000'], 'bbox': [-95.3, 39.8, -91, 43.6], 'start_date': '2008-06-05', 'end_date': '2008-06-15', 'peak_dv_date': '2008-06-09', 'peak_site': '05462000', 'city_geojson_data': {'type': 'FeatureCollection', 'features': [{'type': 'Feature', 'geometry': {'type': 'Point', 'coordinates': []}, 'properties': {'name': 'Cedar Rapids IA', 'country.etc': 'IA', 'pop': '123243', 'capital': '0', 'reftype': 'city'}}]}, 'river_geojson_data': '{"type": "FeatureCollection", "features": [{"type": "Feature", "id": 0, "properties": {"gnis_id": " ", "gnis_name": " ", "reftype": "rivers"}, "geometry": {"type": "MultiLineString", "coordinates": []}}]}', 'background_geojson_data': '{"type": "FeatureCollection", "features": [{"type": "Feature", "geometry": {"type": "Polygon", "coordinates": []}, "properties": {"group": "12", "order": " 2951", "region": "illinois", "reftype": "politicalBoundaries"}}]}'}


        self.mock_path = "mock/path.json"
        self.path = 'flood-viz/examples/reference.json'

        # self.mock_open = mock.mock_open(read_data=self.mock_reference)
        # self.mock_open.return_value = self.mock_response


        self.open_mock = mock.MagicMock(spec=open)
        self.read_mock = mock.MagicMock()
        self.open_mock.return_value.__enter__.return_value = self.mock_reference


    @mock.patch('builtins.open')
    def test_good_data(self, m_open):
        # p = mock.patch.object(builtins, 'open', new_callable=self.mock_open)
        # p.start()
        # with mock.patch('__main__.open', self.mock_open) as m:
        # parsed = parse_reference_data(self.mock_path)
        # self.assertEqual(parsed, self.mock_response)

        # m = mock.mock_open()
        # with mock.patch(parse_reference_data(self.mock_path), m, create=True):
        # self.assertEqual(parse_reference_data(self.mock_path), self.mock_response)


        with mock.patch.object(reference_parser, 'open', self.open_mock, create=True) as m:
            self.assertEqual((reference_parser.parse_reference_data(self.mock_path)), self.mock_response)


