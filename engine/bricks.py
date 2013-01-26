import json
from model import Exit


class Brick(object):
    def __init__(self, db):
        self.db = db

    def get_looks(self, brick, player):
        pass

    def process_and_exit(self, brick, player, input_data):
        pass


class SimpleExit(Brick):
    def __init__(self, db):
        Brick.__init__(self, db)

    def get_looks(self, brick, player):
        data = json.loads(brick.data)
        return data['description']

    def process_input(self, brick, player, input_data):
        data = json.loads(brick.data)
        query = self.db.query(Exit.dest_location_id)
        query = query.filter_by(location_id=brick.location_id)
        query = query.filter_by(exit_id=data['exit_id'])
        player.location_id = exit.dest_location_id
        self.db.commit()


class BrickFactory(object):
    bricks = {}

    def __init__(self, db):
        self.bricks['simple_exit'] = SimpleExit(db)

    def get_looks(self, brick, player):
        return self.bricks[brick.type].get_looks(brick, player)

    def process_input(self, brick, player, input_data):
        return self.bricks[brick.type].process_input(brick, player, input_data)
