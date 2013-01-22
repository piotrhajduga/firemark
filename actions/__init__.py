from twisted.web.resource import Resource
from twisted.web.static import File
from location import Location
from user import User
from home import HomePage
from builder import Builder
from engine.user import UserService
from engine.location import LocationService


def get_app_resource(db, config):
    resource = Resource()
    resource.putChild('', HomePage())
    resource.putChild('play', Location(LocationService(db)))
    resource.putChild('static', File('static'))
    resource.putChild('user', User(UserService(db, config.password_salt)))
    resource.putChild('builder', Builder())
    return resource
