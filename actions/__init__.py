from twisted.web.resource import Resource
from twisted.web.static import File
from location import Location
from auth import SignIn


def get_app_resource(mongodb):
    resource = Resource()
    resource.putChild('location', Location(mongodb))
    resource.putChild('location', Location(mongodb))
    resource.putChild('static', File('static'))
    auth_resource = Resource()
    auth_resource.putChild('signin', SignIn(mongodb))
    resource.putChild('user', auth_resource)
    return resource
