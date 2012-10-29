import logging
from twisted.web.resource import Resource
from twisted.web.error import NoResource
import json


class Location(Resource):
    children = {}

    def __init__(self, output='JSON'):
        self.output = output

    def render_GET(self, request):
        logging.debug('Get request: %s', request)
        if self.output == 'JSON':
            result = json.dumps(self.__dict__)
            logging.debug('Returning json object as a result: %s', result)
            return result
        logging.warn('Speaking only json at the time')
        return NoResource()

    def getChild(self, name, request):
        logging.warn('No children to this page')
        return self
