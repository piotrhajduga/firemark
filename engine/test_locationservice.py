from unittest import TestCase
from pymongo import Connection
import locationservice as locs


class TestLocationService(TestCase):
    mdb = Connection().unittests

    def setUp(self):
        self.service = locs.LocationService(self.mdb)

    def tearDown(self):
        self.mdb.locations.drop()

    def test_get_by_field(self):
        self.mdb.locations.insert({
            'name': 'Test',
            'exits': {},
            'bricks': [],
            'tags': ['test'],
            })
        actual = self.service.get_by_field('name', 'Test')
        self.assertEquals('Test', actual['name'])
        self.assertEquals({}, actual['exits'])
        self.assertEquals([], actual['bricks'])
        self.assertEquals(['test'], actual['tags'])

    def test_add_exit_to(self):
        locid = self.mdb.locations.insert({
            'name': 'Test',
            'exits': {},
            'bricks': [],
            'tags': ['test'],
            })
        # add_exit_to(location_id, exit_name, destination_id)
        self.service.add_exit_to(locid, 'InfLoop', locid)
        loc = self.mdb.locations.find_one({'_id': locid})
        self.assertIn('InfLoop', loc['exits'])
        self.assertEquals(loc['exits']['InfLoop'], locid)
