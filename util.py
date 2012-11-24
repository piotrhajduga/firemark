from zope.interface import Interface, Attribute, implements
from twisted.python.components import registerAdapter
from twisted.web.server import Session as TwistedSession
from mako.lookup import TemplateLookup


class Session(Interface):
    user = Attribute('Login of logged in user')
    errno = Attribute('Error code or 0 if no error')
    error = Attribute('Error message if error occured')


class SessionImpl(object):
    implements(Session)

    def __init__(self, session):
        self.user = None
        self.errno = 0
        self.error = None


def get_output_type_from_request(request):
    try:
        return str(request.args['output'][0]).upper()
    except KeyError:
        return 'HTML'

registerAdapter(SessionImpl, TwistedSession, Session)

tpl_lookup = TemplateLookup(directories=['templates'],
        output_encoding='utf-8', encoding_errors='replace')

# errors
#NOT_LOGGED_IN = {'errno': 11}
#WRONG_PASSWORD = {'errno': 12}
#EMAIL_REGISTERED = {'errno': 13}
#LOGIN_REGISTERED = {'errno': 14}
#PASSWORD_MISMATCH = {'errno': 15}
#USER_NOT_IN_LOCATION = {'errno': 16}
#LOCATION_NOT_FOUND = {'errno': 17}
