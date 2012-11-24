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
        exits = self.mdb.locations.find_one({'_id': locid})['exits']
        self.assertIn('InfLoop', exits)
        self.assertEquals(exits['InfLoop'], locid)

    def test_get_for_user(self):
        locid = self.mdb.locations.insert({
            'name': 'Test',
            })
        uid = self.mdb.users.insert({
            'email': 'a@a.a',
            'login': 'test',
            'location_id': locid,
            })
        actual = self.service.get_for_user(uid)
        self.assertEquals(actual['_id'], locid)

    def test_get_for_user_not_in_location(self):
        uid = self.mdb.users.insert({
            'email': 'a@a.a',
            'login': 'test',
            })
        self.assertRaises(locs.UserNotInLocation, self.service.get_for_user, uid)

    def test_get_for_user_location_not_found(self):
        uid = self.mdb.users.insert({
            'email': 'a@a.a',
            'login': 'test',
            'location_id': 1,
            })
        self.assertRaises(locs.LocationNotFound, self.service.get_for_user, uid)
