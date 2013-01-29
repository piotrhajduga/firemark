from model import Location


class LocationBuilderService(object):
    db = None

    def __init__(self, db):
        self.db = db

    def new_location(self, name, user):
        loc = Location(name)
        loc.owner_user_id = user.id
        self.db.add(loc)
        self.db.commit()
        return loc
