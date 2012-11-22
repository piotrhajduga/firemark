import logging
from twisted.web.resource import Resource
from mako.template import Template
import json
import util


def get_output_type_from_request(request):
    try:
        return str(request.args['output'][0]).upper()
    except KeyError:
        return 'HTML'


class Location(Resource):
    isLeaf = True
    template_HTML = Template(filename='templates/location.html')

    def __init__(self, mongodb):
        Resource.__init__(self)
        self.locations = mongodb.locations
        self.players = mongodb.players

    def render_GET(self, request):
        type_key = get_output_type_from_request(request)
        if type_key == 'JSON':
            return self.render_JSON(request)
        else:  # type_key == 'HTML'
            return self.render_HTML(request)

    def render_HTML(self, request):
        try:
            player = self.get_player(request)
            location = self.get_location(player)
            data = {'location': location, 'player': player}
        except UserWarning:
            data = {'errno': 11, 'error': 'Not logged in!'}
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(**data).encode('utf-8')

    def render_JSON(self, request):
        try:
            player = self.get_player(request)
            location = self.get_location(player)
            data = {'location': location}
        except UserWarning:
            data = {'errno': 11, 'error': 'Not logged in!'}
        request.setHeader("Content-Type", "text/plain; charset=utf-8")
        return json.dumps(data).encode('utf-8')

    def get_player(self, request):
        login = util.User(request.getSession()).login
        if login is None:
            logging.warn('User not logged in!')
            raise UserWarning('Not logged in!')
        logging.debug('Logged user: %s', login)
        return self.players.find_one({'login': login})

    def get_location(self, player):
        return self.locations.find_one({'_id': player['location_id']})
