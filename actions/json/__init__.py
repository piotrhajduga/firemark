from twisted.web.resource import Resource
from actions.json.user import User
from actions.json.location import Location
from actions.json.builder import Builder
from engine.user import UserService
from engine.location import LocationService


def get_app_resource(db, config):
    resource = Resource()
    resource.putChild('user', User(UserService(db, config.password_salt)))
    resource.putChild('location', Location(LocationService(db)))
    resource.putChild('builder', Builder(LocationService(db)))
    return resource
