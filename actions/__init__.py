from twisted.web.resource import Resource
from twisted.web.static import File
from location import Location


def get_app_resource(mongodb):
    resource = Resource()
    resource.putChild('location', Location(mongodb))
    resource.putChild('static', File('static'))
    return resource
