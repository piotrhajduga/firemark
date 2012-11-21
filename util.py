from zope.interface import Interface
from zope.interface import Attribute
from zope.interface import implements
from twisted.python.components import registerAdapter
from twisted.web.server import Session


class User(Interface):
    login = Attribute('Login of logged in user')


class UserImpl(object):
    implements(User)

    def __init__(self, session):
        self.login = None

registerAdapter(UserImpl, Session, User)

# errors
NOT_LOGGED_IN = {'errno': 11, 'message': 'Not logged in!'}
