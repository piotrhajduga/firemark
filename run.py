from twisted.web.resource import Resource
from twisted.web.error import NoResource
from twisted.web.server import Site
from twisted.internet import reactor
import actions.location


class JSON(Resource):
    def getChild(self, name, request):
        if str(name).lower() == 'location':
            return actions.location.Location(output='JSON')
        return NoResource()


class Engine(Resource):
    def getChild(self, name, request):
        if str(name).lower() == 'json':
            return JSON()
        return NoResource()

root = Engine()
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
