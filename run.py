#!/usr/bin/env python2.7
import logging
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor
from pymongo import Connection
import actions


log_format = '%(asctime)s %(levelname)7s [%(module)s %(lineno)d %(funcName)s] %(message)s'
logging.basicConfig(level='DEBUG', format=log_format)

mongo = Connection()
mdb = mongo.firemark

root = Resource()
root.putChild('action', actions.get_resource(mdb))

logging.info('Listening on the port %d', 8880)
reactor.listenTCP(8880, Site(root))
logging.info('Running the instance')
reactor.run()
