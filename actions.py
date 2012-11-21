import logging
from twisted.web.resource import Resource
from twisted.web.error import NoResource
import json
import util


class Action(Resource):
    renderers = {}

    def __init__(self):
        Resource.__init__(self)

    def render_data(self, request, data):
        logging.info('GET REQUEST: %s', request)
        logging.debug('HEADERS: %s', request.getAllHeaders())
        logging.debug('GET ARGS: %s', request.args)
        try:
            try:
                type_key = str(request.args['output'][0]).upper()
            except KeyError:
                type_key = 'HTML'
            render = self.renderers[type_key]
            logging.info('Returning %s string as a result', type_key)
            return render(data)
        except KeyError:
            logging.exception('Cannot find renderer for type %s', type_key)
        return 'Cannot render data in type %s' % type_key


class Location(Action):
    def __init__(self, mongodb):
        Action.__init__(self)
        self.locations = mongodb.locations
        self.players = mongodb.players
        self.renderers['HTML'] = lambda data: str(data)
        self.renderers['JSON'] = json.dumps

    def render_GET(self, request):
        login = util.User(request.getSession()).login
        if login is None:
            logging.warn('User not logged in!')
            return self.render_data(request, util.NOT_LOGGED_IN)
        logging.info('Logged user: %s', login)
        player = self.players.find_one({'login': login})
        location = self.locations.find_one({'_id': player['location_id']})
        return self.render_data(request, data=location)

    def getChild(self, name, request):
        logging.warn('No children to this page')
        return NoResource()


# actions resources resource
def get_resource(mongodb):
    resource = Resource()
    resource.putChild('location', Location(mongodb))
    return resource
