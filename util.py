from zope.interface import Interface
from zope.interface import Attribute
from zope.interface import implements
from twisted.python.components import registerAdapter
from twisted.web.server import Session
from mako.lookup import TemplateLookup


class User(Interface):
    login = Attribute('Login of logged in user')


class UserImpl(object):
    implements(User)

    def __init__(self, session):
        self.login = None


def get_output_type_from_request(request):
    try:
        return str(request.args['output'][0]).upper()
    except KeyError:
        return 'HTML'

registerAdapter(UserImpl, Session, User)

tpl_lookup = TemplateLookup(directories=['templates'],
        output_encoding='utf-8', encoding_errors='replace')

# errors
NOT_LOGGED_IN = {'errno': 11, 'message': 'Not logged in!'}
