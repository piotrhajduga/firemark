from model import Exit, Player


class UserNotInLocation(Exception):
    pass


class LocationNotFound(Exception):
    pass


class LocationService(object):
    db = None

    def __init__(self, db):
        self.db = db

    def add_exit_to(self, location_id, exit_name, destination_id):
        exit = Exit(exit_name)
        exit.location_id = location_id
        exit.dest_location_id = destination_id
        self.db.add(exit)
        self.db.commit()
        return exit

    def get_for_user(self, user_id):
        player = self.db.query(Player).filter(Player.user_id == user_id).one()
        return player.location

    def get_starting_location(self):
        location = {}
        location['_id'] = 0
        location['name'] = 'Start the adventure!'
        location['exits'] = {}
        starting = self.locs.find({'starting': 1})
        for loc in starting:
            location['exits'][loc['_id']] = loc
        return location

    def get_exit_for_user(self, exit_name, user_id):
        loc = self.get_for_user(user_id)
        return loc['exits'][exit_name]
