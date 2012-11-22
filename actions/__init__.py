from twisted.web.resource import Resource
from location import Location

def get_app_resource(mongodb):
    resource = Resource()
    resource.putChild('location', Location(mongodb))
    return resource
