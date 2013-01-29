from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Location
from engine.builder import LocationBuilderService


class TestLocationService(TestCase):
    db = None
    service = None

    def setUp(self):
        db_engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(db_engine)
        Session = sessionmaker(bind=db_engine)
        self.db = Session()
        self.service = LocationBuilderService(Session())

    def tearDown(self):
        self.db.close()

    def test_create_location(self):
        name = 'test'
        user_id = 3
        loc = self.service.create_location(name, user_id)
        self.assertEquals(loc['name'], name)
        self.assertEquals(loc['owner_user_id'], user_id)
        query = self.db.query(Location)
        query = query.filter_by(owner_user_id=user_id)
        query = query.filter_by(name=name)
        self.assertEquals(query.count(), 1)
