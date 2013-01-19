from twisted.web.resource import Resource
from twisted.web.static import File
from location import Location
from user import User
from home import HomePage
from engine import userservice as usrs
from engine import locationservice as locs


def get_app_resource(mongodb):
    resource = Resource()
    resource.putChild('', HomePage())
    resource.putChild('play', Location(locs.LocationService(mongodb)))
    resource.putChild('static', File('static'))
    resource.putChild('user', User(usrs.UserService(mongodb)))
    return resource
