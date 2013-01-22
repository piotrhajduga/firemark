from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Location, Exit, Brick
from engine.location import LocationService


class TestLocationService(TestCase):
    session = None
    service = None

    def setUp(self):
        db_engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(db_engine)
        Session = sessionmaker(bind=db_engine)
        self.session = Session()
        self.service = LocationService(Session())

    def tearDown(self):
        self.session.close()

    def test_add_exit_to(self):
        loc = Location('TestLoc')
        self.session.add(loc)
        self.session.commit()
        # add_exit_to(location_id, exit_name, destination_id)
        exit = self.service.add_exit_to(
                loc.location_id,
                'InfLoop',
                loc.location_id
                )
        self.assertIsNotNone(exit)
        query = self.session.query(Exit)
        query = query.filter(Exit.location_id == loc.location_id)
        query = query.filter(Exit.dest_location_id == loc.location_id)
        query = query.filter(Exit.name == 'InfLoop')
        self.assertIsNotNone(query.one())

    def test_get_for_user(self):
        locid = self.mdb.locations.insert({'name': 'Test'})
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

    def test_get_starting_location(self):
        self.mdb.locations.insert({'name': 'Test'})
        self.mdb.locations.insert({'name': 'Test'})
        self.mdb.locations.insert({'name': 'Test', 'starting': 1})
        self.mdb.locations.insert({'name': 'Test', 'starting': 1})
        self.mdb.locations.insert({'name': 'Test', 'starting': 1})
        loc = self.service.get_starting_location()
        self.assertIsNotNone(loc)
        self.assertEquals(len(loc['exits']), 3)
