from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Location, Exit, User, Player, Namespace
from engine.location import LocationService, PlayerNotInLocation, LocationNotFound


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
        exit = self.service.add_exit_to(loc.id, loc.id)
        self.assertIsNotNone(exit)
        query = self.db.query(Exit).filter_by(
            location_id=loc.id, dest_location_id=loc.id)
        self.assertIsNotNone(query.one())

    def test_get_for_player(self):
        location = Location('test')
        self.db.add(location)
        user = User('test', 'test@test.com', 'test')
        self.db.add(user)
        self.db.commit()
        player = Player()
        player.user_id = user.id
        player.location_id = location.id
        self.db.add(player)
        self.db.commit()
        location_actual = self.service.get_for_player(player.id)
        self.assertEquals(location_actual.id, location.id)

    def test_get_for_user_not_in_location(self):
        user = User('test', 'test@test.com', 'test')
        self.db.add(user)
        self.db.commit()
        player = Player()
        player.user_id = user.id
        self.db.add(player)
        self.db.commit()
        self.assertRaises(PlayerNotInLocation,
                          self.service.get_for_player, player.id)

    def test_get_for_user_location_not_found(self):
        user = User('test', 'test@test.com', 'test')
        self.db.add(user)
        self.db.commit()
        player = Player()
        player.user_id = user.id
        player.location_id = 100
        self.db.add(player)
        self.db.commit()
        self.assertRaises(LocationNotFound,
                          self.service.get_for_player, player.id)

    def test_get_starting_location(self):
        locations = [Location('Test 1'),
                     Location('Test 2'),
                     Location('Test 3'),
                     Location('Test 4'),
                     Location('Test 5'),
                     ]
        self.db.add_all(locations)
        namespace = Namespace('starting', starting=True)
        self.db.add(namespace)
        self.db.commit()
        locations_expected = [locations[1],
                              locations[2],
                              locations[4],
                              ]
        namespace.locations = locations_expected
        self.db.commit()
        location_actual = self.service.get_starting_location()
        self.assertIn(location_actual.id,
                      map(lambda loc: loc.id, locations_expected))

    def test_search_name_like(self):
        locations_expected = [Location('Test'),
                              Location('TeSt'),
                              Location('TEST'),
                              Location('tEST'),
                              Location('test'),
                              ]
        self.db.add_all(locations_expected)
        self.db.add(Location('zosi'))
        self.db.commit()
        locations_actual = self.service.search(name_like='test')
        self.assertEqual(map(lambda loc: loc.id, locations_actual),
                         map(lambda loc: loc.id, locations_expected))
