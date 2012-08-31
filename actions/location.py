from twisted.web.resource import Resource
from twisted.web.error import NoResource
import json


class Location(Resource):
    def __init__(self, output='JSON'):
        self.output = output

    def render_GET(self, request):
        if self.output == 'JSON':
            return json.dumps(self.__dict__)
        return NoResource()
