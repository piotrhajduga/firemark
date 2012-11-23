from twisted.web.resource import Resource
from twisted.web.static import File
from location import Location
from user import SignIn, SignUp
from engine import userservice as usrs


def get_app_resource(mongodb):
    resource = Resource()
    resource.putChild('location', Location(mongodb))
    resource.putChild('location', Location(mongodb))
    resource.putChild('static', File('static'))
    auth_resource = Resource()
    auth_resource.putChild('signin', SignIn(usrs.UserService(mongodb)))
    auth_resource.putChild('signup', SignUp(usrs.UserService(mongodb)))
    resource.putChild('user', auth_resource)
    return resource
