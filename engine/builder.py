from model import Location


class LocationBuilderService(object):
    db = None

    def __init__(self, db):
        self.db = db

    def create_location(self, name, user_id):
        loc = Location(name)
        loc.owner_user_id = user_id
        self.db.add(loc)
        self.db.commit()
        return loc.get_dict()

    def get_location_data(self, loc_id):
        raise NotImplementedError()

    def get_location_namespaces(self, loc_id):
        raise NotImplementedError()

    def get_location_bricks(self, loc_id):
        raise NotImplementedError()

    def set_name(self, loc_id, name):
        raise NotImplementedError()
