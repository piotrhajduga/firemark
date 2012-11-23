from twisted.web.resource import Resource
from twisted.web.static import File
from location import Location
from user import SignIn, SignUp
from home import HomePage
from engine import userservice as usrs


def get_app_resource(mongodb):
    resource = Resource()
    resource.putChild('location', Location(mongodb))
    resource.putChild('location', Location(mongodb))
    resource.putChild('static', File('static'))
    resource.putChild('', HomePage())
    user_resource = Resource()
    user_resource.putChild('signin', SignIn(usrs.UserService(mongodb)))
    user_resource.putChild('signup', SignUp(usrs.UserService(mongodb)))
    resource.putChild('user', user_resource)
    return resource
