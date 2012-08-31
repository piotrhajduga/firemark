from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor
import actions.location


jsonResource = Resource()
jsonResource.putChild('location', actions.location.Location(output='JSON'))

root = Resource()
root.putChild('json', jsonResource)
factory = Site(root)
reactor.listenTCP(8880, factory)
reactor.run()
