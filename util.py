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


class Service(object):
    #TODO: services should extend this class!!!
    def __init__(self, db, config):
        self.db = db
        self.config = config


class ServicesFactory(object):
    services = {}

    def __init__(self, database):
        self.database = database

    def inject(self, service_name):
        try:
            return self.services[service_name]
        except KeyError:
            service_class = __import__(service_name)
            self.services[service_name] = service_class(self.database)
            return self.services[service_name]


registerAdapter(SessionImpl, TwistedSession, Session)
