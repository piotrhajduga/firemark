#!/usr/bin/env python2.7
import logging
from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor
from pymongo import Connection
import actions
import config as cfg


logging.basicConfig(level=cfg.log_level, format=cfg.log_format)

mongo = Connection()
mdb = mongo[cfg.mdb_name]

root = Resource()
root.putChild('action', actions.get_resource(mdb))

logging.info('Listening on the port %d', cfg.http_port)
reactor.listenTCP(cfg.http_port, Site(root))
logging.info('Running the instance')
reactor.run()
