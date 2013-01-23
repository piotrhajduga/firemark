from twisted.web.resource import Resource
from twisted.web.static import File
from actions.location import Location
from actions.user import User
from actions.home import HomePage
from actions.builder import Builder
from engine.user import UserService
from engine.location import LocationService
import actions.json


def get_app_resource(db, config):
    resource = Resource()
    resource.putChild('', HomePage())
    resource.putChild('play', Location(LocationService(db)))
    resource.putChild('static', File('static'))
    resource.putChild('user', User(UserService(db, config.password_salt)))
    resource.putChild('builder', Builder(LocationService(db)))
    resource.putChild('json', actions.json.get_app_resource(db, config))
    return resource
