from zope.interface import Interface, Attribute, implements
from twisted.python.components import registerAdapter
from twisted.web.server import Session as TwistedSession


class Session(Interface):
    user = Attribute('Logged in user')
    errno = Attribute('Error code or 0 if no error')
    error = Attribute('Error message if error occured')
    data = Attribute('Additional data to hold in session if needed')


class SessionImpl(object):
    implements(Session)

    def __init__(self, session):
        self.user = None
        self.errno = 0
        self.error = None
        self.data = None


registerAdapter(SessionImpl, TwistedSession, Session)
