from unittest import TestCase
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Brick, Player, Location, Exit
from engine.bricks import BrickService
import json


class TestBrickService(TestCase):
    db = None
    service = None

    def setUp(self):
        db_engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(db_engine)
        Session = sessionmaker(bind=db_engine)
        self.db = Session()
        self.service = BrickService(Session())

    def tearDown(self):
        self.db.close()


class TestSimpleExit(TestBrickService):
    type = 'simple_exit'

    def test_get_brick_types(self):
        self.assertIn(self.type, self.service.get_brick_types())

    def test_set_config(self):
        brick = Brick(self.type)
        self.db.add(brick)
        self.db.commit()
        self.service.set_config(brick, exit_id=2, description='test')
        self.assertEquals(json.loads(brick.data)['exit_id'], 2)
        self.assertEquals(json.loads(brick.data)['description'], 'test')

    def test_get_looks(self):
        description = 'test brick'
        brick = Brick(self.type)
        brick.data = json.dumps({'description': description})
        self.assertEquals(self.service.get_looks(brick, player=Player()),
                          description)

    def test_process_input(self):
        locs = [Location('src'), Location('dest')]
        self.db.add_all(locs)
        self.db.commit()
        exit_ = Exit()
        exit_.location_id = locs[0].id
        exit_.dest_location_id = locs[1].id
        self.db.add(exit_)
        self.db.commit()
        brick = Brick(self.type)
        brick.location_id = locs[0].id
        brick.data = json.dumps({'exit_id': exit_.id})
        player = Player()
        player.location_id = locs[0].id
        self.db.add(brick)
        self.db.add(player)
        self.db.commit()
        self.assertEquals(player.location_id, locs[0].id)
        self.service.process_input(brick, player, input_data={})
        self.assertEquals(player.location_id, locs[1].id)


class TestDescription(TestBrickService):
    type = 'description'

    def test_get_brick_types(self):
        self.assertIn(self.type, self.service.get_brick_types())

    def test_set_config(self):
        brick = Brick(self.type)
        self.db.add(brick)
        self.db.commit()
        self.service.set_config(brick, content='test')

    def test_get_looks(self):
        content = 'test brick'
        brick = Brick(self.type)
        brick.data = json.dumps({'content': content})
        self.assertEquals(self.service.get_looks(brick, Player()), content)

    def test_process_input(self):
        brick = Brick(self.type)
        self.assertRaises(NotImplementedError, self.service.process_input,
                          brick=brick, player=Player(), input_data={})


class TestRegexInput(TestBrickService):
    type = 'regex_input'

    def test_get_brick_types(self):
        self.assertIn(self.type, self.service.get_brick_types())

    def test_set_config(self):
        brick = Brick(self.type)
        self.db.add(brick)
        self.db.commit()
        self.service.set_config(brick, label='test', regex='test',
                                match=2, nomatch=3)
        self.assertEquals(json.loads(brick.data)['label'], 'test')
        self.assertEquals(json.loads(brick.data)['regex'], 'test')
        self.assertEquals(json.loads(brick.data)['match'], 2)
        self.assertEquals(json.loads(brick.data)['nomatch'], 3)

    def test_get_looks(self):
        label = 'test brick'
        brick = Brick(self.type)
        brick.data = json.dumps({'label': label})
        self.assertEquals(self.service.get_looks(brick, player=Player()),
                          label)

    def test_process_input(self):
        locs = [Location('source'), Location('match'), Location('nomatch')]
        self.db.add_all(locs)
        self.db.commit()
        player = Player()
        player.location_id = locs[0].id
        self.db.add(player)
        brick = Brick(self.type)
        brick.location_id = locs[0].id
        self.db.add(brick)
        exits = [Exit(), Exit()]
        exits[0].location_id = locs[0].id
        exits[0].dest_location_id = locs[1].id
        exits[1].location_id = locs[0].id
        exits[1].dest_location_id = locs[2].id
        self.db.add_all(exits)
        self.db.commit()
        self.service.set_config(brick, label='test', regex='^ugab[aueo]+ga$',
                                match=exits[0].id, nomatch=exits[1].id)
        self.service.process_input(brick, player, {'input': 'ugabaga'})
        self.assertEquals(player.location_id, locs[1].id)
        player.location_id = locs[0].id
        self.db.commit()
        self.service.process_input(brick, player, {'input': 'ugabxga'})
        self.assertEquals(player.location_id, locs[2].id)
