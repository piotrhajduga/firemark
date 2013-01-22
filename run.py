#!/usr/bin/env python2.7
import logging
from twisted.web.server import Site
from twisted.internet import reactor
from sqlalchemy import create_engine
from model import Base
from sqlalchemy.orm import sessionmaker
import config as cfg
import actions


logging.basicConfig(level=cfg.log_level, format=cfg.log_format)
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

db_engine = create_engine(cfg.db_url,
        echo=cfg.db_echo, encoding=cfg.db_encoding)
Base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)

root = actions.get_app_resource(Session())

logging.info('Listening on the port %d', cfg.http_port)
reactor.listenTCP(cfg.http_port, Site(root))
logging.info('Running the instance')
reactor.run()
