#!/usr/bin/env python2.7
import logging
from twisted.web.server import Site
from twisted.internet import reactor
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
import config as cfg
import views


logging.basicConfig(level=cfg.log_level, format=cfg.log_format)
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARN)
logging.getLogger('sqlalchemy.orm').setLevel(logging.WARN)

db_engine = create_engine(cfg.db_url, echo=cfg.db_echo,
                          encoding=cfg.db_encoding)
Base.metadata.create_all(db_engine)
Session = sessionmaker(bind=db_engine)

root = views.get_app_resource(Session(), cfg)

logging.info('Listening on the port %d', cfg.http_port)
reactor.listenTCP(cfg.http_port, Site(root))
logging.info('Running the instance')
reactor.run()
