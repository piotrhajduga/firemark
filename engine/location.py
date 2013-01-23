from model import Exit, Player, Location


class PlayerNotInLocation(Exception):
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
        if not player.location_id:
            raise PlayerNotInLocation()
        if player.location:
            return player.location
        else:
            raise LocationNotFound()

    def get_starting_location(self):
        query = self.db.query(Location).filter(Location.tags.like('%starting%'))
        return query.one()

    def get_exit_for_user(self, exit_name, user_id):
        loc = self.get_for_user(user_id)
        return loc['exits'][exit_name]

    def get_for_tag(self, tag):
        query = self.db.query(Location).filter(Location.tags.like('%' + tag + '%'))
        return filter(lambda loc: tag in loc.get_tags(), query.all())
