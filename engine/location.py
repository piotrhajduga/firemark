from model import Player, Location, Namespace
from exc import PlayerNotInLocation, LocationNotFound
import random


class LocationService(object):
    db = None

    def __init__(self, db):
        self.db = db

    def get_for_player(self, player_id):
        player = self.db.query(Player).get(player_id)
        if not player.location_id:
            raise PlayerNotInLocation()
        if player.location:
            return player.location
        else:
            raise LocationNotFound()

    def get_starting_location(self):
        locations = self.db.query(Location).filter(
            Location.namespaces.any(Namespace.starting)).all()
        if not locations:
            raise LocationNotFound()
        return random.choice(locations)

    def get_exit_for_user(self, exit_name, user_id):
        loc = self.get_for_user(user_id)
        return loc['exits'][exit_name]

    def search(self, **kwargs):
        namespace_id = kwargs.get('namespace_id', None)
        name_like = kwargs.get('name_like', None)
        query = self.db.query(Location)
        if namespace_id:
            query = query.filter(Location.namespaces.any(
                Namespace.id == namespace_id))
        if name_like:
            query = query.filter(Location.name.like(name_like))
        return query.all()
