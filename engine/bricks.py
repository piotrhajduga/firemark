import json
import re
from model import Exit, Brick


class BrickBase(object):
    def __init__(self, db):
        self.db = db

    def get_looks(self, brick, player):
        """Get initial data to display brick.

        brick -- model.Brick instance that is shown
        player -- model.Player instance for current player
        """
        raise NotImplementedError()

    def process_input(self, brick, player, input_data):
        """Process input data from the user and set player's new location.

        The implementation of this method should call SQLAlchemy's
        session.commit() itself if it's needed.

        brick -- model.Brick instance that performs the processing
        player -- model.Player instance for current player
        input_data -- input data taken from user
        """
        raise NotImplementedError()

    def set_config(self, brick, **kwargs):
        """Apply configuration to brick model.

        The implementation of this method should call SQLAlchemy's
        session.commit() itself.

        brick -- model.Brick instance to change
        **kwargs -- configuration parameters for the brick
        """
        raise NotImplementedError()

    def get_config(self, brick):
        """Get the configuration data for brick as a dict.

        brick -- model.Brick instance to change
        """
        return json.loads(brick.data) if brick.data else {}


class SimpleExit(BrickBase):
    def get_looks(self, brick, player=None):
        data = json.loads(brick.data)
        return data['description']

    def process_input(self, brick, player, input_data):
        data = self.get_config(brick)
        query = self.db.query(Exit).select_from(Brick).join(Brick.exits)
        query = query.filter(Brick.id == brick.id)
        query = query.filter(Exit.id == data['exit_id'])
        player.location_id = query.one().dest_location_id
        self.db.commit()

    def set_config(self, brick, **kwargs):
        data = self.get_config(brick)
        data['description'] = kwargs['description']
        data['exit_id'] = kwargs['exit_id']
        brick.data = json.dumps(data)
        self.db.commit()


class Description(BrickBase):
    def get_looks(self, brick, player):
        data = self.get_config(brick)
        return data['content']

    def set_config(self, brick, **kwargs):
        data = self.get_config(brick)
        data['content'] = kwargs['content']
        brick.data = json.dumps(data)
        self.db.commit()


class RegexInput(BrickBase):
    def get_looks(self, brick, player):
        data = self.get_config(brick)
        return data['label']

    def process_input(self, brick, player, input_data):
        data = self.get_config(brick)
        match = re.match(data['regex'], input_data['input'])
        exit_id = data['match'] if match else data['nomatch']
        query = self.db.query(Exit).select_from(Brick).join(Brick.exits)
        query = query.filter(Brick.id == brick.id)
        query = query.filter(Exit.id == exit_id)
        player.location_id = query.one().dest_location_id
        self.db.commit()

    def set_config(self, brick, **kwargs):
        data = self.get_config(brick)
        data['label'] = kwargs['label']
        data['regex'] = kwargs['regex']
        data['match'] = kwargs['match']
        data['nomatch'] = kwargs['nomatch']
        brick.data = json.dumps(data)
        self.db.commit()


class BrickService(object):
    bricks = {}

    def __init__(self, db):
        self.bricks['simple_exit'] = SimpleExit(db)
        self.bricks['description'] = Description(db)
        self.bricks['regex_input'] = RegexInput(db)

    def get_brick_types(self):
        return self.bricks.keys()

    def get_looks(self, brick, player):
        """Get initial data to display brick.

        brick -- model.Brick instance that is shown
        player -- model.Player instance for current player
        """
        return self.bricks[brick.type].get_looks(brick, player)

    def process_input(self, brick, player, input_data):
        """Process input data from the user and set player's new location.

        The implementation should call SQLAlchemy's session.commit() itself
        if it's needed.

        brick -- model.Brick instance that performs the processing
        player -- model.Player instance for current player
        input_data -- input data taken from user
        """
        return self.bricks[brick.type].process_input(brick, player, input_data)

    def set_config(self, brick, **kwargs):
        """Apply configuration to brick model.

        brick -- model.Brick instance to change
        **kwargs -- configuration parameters for the brick
        """
        return self.bricks[brick.type].set_config(brick, **kwargs)

    def get_config(self, brick, **kwargs):
        """Get the configuration data for brick as a dict.

        brick -- model.Brick instance to change
        """
        return self.bricks[brick.type].get_config(brick)
