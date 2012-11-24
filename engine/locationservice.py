class UserNotInLocation(Exception):
    pass


class LocationNotFound(Exception):
    pass


class LocationService(object):
    _mdb = None
    locs = None

    def __init__(self, mongodb):
        self._mdb = mongodb
        self.locs = self._mdb.locations

    def get_by_field(self, key, value):
        return self.locs.find_one({key: value})

    def add_exit_to(self, location_id, exit_name, destination_id):
        exits = self.locs.find_one({'_id': location_id})['exits']
        exits[exit_name] = destination_id
        self.locs.update({'_id': location_id}, {'$set': {'exits': exits}})

    def get_for_user(self, user_id):
        try:
            locid = self._mdb.users.find_one({'_id': user_id})['location_id']
        except KeyError:
            locid = None
        if not locid:
            raise UserNotInLocation()
        loc = self.locs.find_one({'_id': locid})
        if not loc:
            raise LocationNotFound()
        return loc

    def get_starting_location(self):
        pass

    def get_exit_for_user(exit_name, user_id):
        pass
