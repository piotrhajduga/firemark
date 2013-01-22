from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Location, Exit, Brick, User, Player
from engine.location import LocationService


class TestLocationService(TestCase):
    db = None
    service = None

    def setUp(self):
        db_engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(db_engine)
        Session = sessionmaker(bind=db_engine)
        self.db = Session()
        self.service = LocationService(Session())

    def tearDown(self):
        self.db.close()

    def test_add_exit_to(self):
        loc = Location('TestLoc')
        self.db.add(loc)
        self.db.commit()
        # add_exit_to(location_id, exit_name, destination_id)
        exit = self.service.add_exit_to(
                loc.location_id,
                'InfLoop',
                loc.location_id
                )
        self.assertIsNotNone(exit)
        query = self.db.query(Exit)
        query = query.filter(Exit.location_id == loc.location_id)
        query = query.filter(Exit.dest_location_id == loc.location_id)
        query = query.filter(Exit.name == 'InfLoop')
        self.assertIsNotNone(query.one())

    def test_get_for_user(self):
        location = Location('test', 'starting')
        self.db.add(location)
        user = User('test', 'test@test.com', 'test')
        self.db.add(user)
        self.db.commit()
        player = Player()
        player.user_id = user.user_id
        player.location_id = location.location_id
        self.db.add(player)
        self.db.commit()
        loc = self.service.get_for_user(user.user_id)
        self.assertEquals(loc.location_id, location.location_id)

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
