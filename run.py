#!/usr/bin/env python2.7
import logging
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor
import actions.location


log_format = '%(asctime)s %(levelname)s [%(module)s %(lineno)d %(funcName)s] %(message)s'
logging.basicConfig(level='DEBUG', format=log_format)

jsonResource = Resource()
jsonResource.putChild('location', actions.location.Location(output='JSON'))

root = Resource()
root.putChild('json', jsonResource)

factory = Site(root)
logging.info('Listening on the port %d', 8880)
reactor.listenTCP(8880, factory)
logging.info('Running the instance')
reactor.run()
