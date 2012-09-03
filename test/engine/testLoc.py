import unittest
import pymongo


class LocationService(unittest.TestCase):
    def setUp(self):
        con = pymongo.Connection()
        mdb = con.test
        self.location_service = LocationService(mdb)

    def testAddLocation(self):
        new_location = {
                u'name': u'TestName1',
                u'desc': u'TestDesc1',
                u'bricks': [
                    {u'type': u'text', u'value': u'test'},
                    {u'type': u'exit', u'value': u'1'},
                    ],
                }
        new_id = self.location_service.add_location(new_location)
        self.assertIsNotNone(new_id)
        self.assertGreater(new_id, 0)
