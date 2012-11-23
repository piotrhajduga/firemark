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
