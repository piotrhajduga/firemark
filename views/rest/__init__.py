from twisted.web.resource import Resource
from views.rest.user import User
from views.rest.location import Location
from views.rest.builder import Builder
from engine.user import UserService
from engine.location import LocationService


def get_app_resource(db, config):
    resource = Resource()
    resource.putChild('user', User(UserService(db, config.password_salt)))
    resource.putChild('location', Location(LocationService(db)))
    resource.putChild('builder', Builder(LocationService(db)))
    return resource
