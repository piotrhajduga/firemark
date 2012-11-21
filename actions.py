import logging
from twisted.web.resource import Resource
from twisted.web.error import NoResource
import json
import util


def get_output_type_from_request(request):
    try:
        return str(request.args['output'][0]).upper()
    except KeyError:
        return 'HTML'


class Renderer(object):
    renderers = {}

    def get_output(self, type_key, data):
        try:
            render = self.renderers[type_key]
            return render(data)
        except KeyError:
            logging.exception('Cannot find renderer for type %s', type_key)
            return None


class Location(Resource):
    renderer = Renderer()

    def __init__(self, mongodb):
        Resource.__init__(self)
        self.locations = mongodb.locations
        self.players = mongodb.players
        self.renderer.renderers['HTML'] = lambda data: str(data)
        self.renderer.renderers['JSON'] = json.dumps

    def render_GET(self, request):
        type_key = get_output_type_from_request(request)
        login = util.User(request.getSession()).login
        if login is None:
            logging.warn('User not logged in!')
            return self.renderer.get_output(type_key, util.NOT_LOGGED_IN)
        logging.info('Logged user: %s', login)
        player = self.players.find_one({'login': login})
        location = self.locations.find_one({'_id': player['location_id']})
        logging.debug('Trying to render %s string as a result', type_key)
        return self.renderer.get_output(type_key, data=location)

    def getChild(self, name, request):
        logging.warn('No children to this page')
        return NoResource()


# actions resources resource
def get_resource(mongodb):
    resource = Resource()
    resource.putChild('location', Location(mongodb))
    return resource
