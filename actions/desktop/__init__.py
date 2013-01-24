from twisted.web.resource import Resource
from engine.user import UserService
from engine.location import LocationService
from mako.lookup import TemplateLookup
# controllers for this package
from location import Location
from user import User
from home import HomePage
from builder import Builder


tpl_lookup = TemplateLookup(directories=['templates/desktop'],
        output_encoding='utf-8', encoding_errors='replace')


def get_app_resource(db, config):
    resource = Resource()
    resource.putChild('', HomePage())
    resource.putChild('play', Location(LocationService(db)))
    resource.putChild('user', User(UserService(db, config.password_salt)))
    resource.putChild('builder', Builder(LocationService(db)))
    return resource
