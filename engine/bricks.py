import json
from model import Exit


class Brick(object):
    def __init__(self, db):
        self.db = db

    def get_looks(self, brick, player):
        """Get initial data to display brick.

        brick -- model.Brick instance that is shown
        player -- model.Player instance for current player
        """
        raise NotImplemented()

    def process_and_exit(self, brick, player, input_data):
        """Process input data from the user and set player's new location.

        The implementation should call SQLAlchemy's session.commit() itself
        if it's needed.

        brick -- model.Brick instance that performs the processing
        player -- model.Player instance for current player
        input_data -- input data taken from user
        """
        raise NotImplemented()

    def set_config(self, brick, **kwargs):
        """Apply configuration to brick model.

        The implementation should call SQLAlchemy's session.commit() itself.

        brick -- model.Brick instance to change
        **kwargs -- configuration parameters for the brick
        """
        raise NotImplemented()


class SimpleExit(Brick):
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

    def set_config(self, brick, **kwargs):
        data = {}
        data['description'] = kwargs['description']
        data['exit_id'] = kwargs['exit_id']
        brick.data = json.dumps(data)
        self.db.commit()


class BrickFactory(object):
    bricks = {}

    def __init__(self, db):
        self.bricks['simple_exit'] = SimpleExit(db)

    def get_looks(self, brick, player):
        return self.bricks[brick.type].get_looks(brick, player)

    def process_input(self, brick, player, input_data):
        return self.bricks[brick.type].process_input(brick, player, input_data)

    def set_config(self, brick, **kwargs):
        return self.bricks[brick.type].set_config(brick, **kwargs)
