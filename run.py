#!/usr/bin/env python2.7
import logging
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor
import actions


log_format = '%(asctime)s %(levelname)s [%(module)s %(lineno)d %(funcName)s] %(message)s'
logging.basicConfig(level='DEBUG', format=log_format)

root = Resource()
root.putChild('action', actions.resources)

logging.info('Listening on the port %d', 8880)
reactor.listenTCP(8880, Site(root))
logging.info('Running the instance')
reactor.run()
