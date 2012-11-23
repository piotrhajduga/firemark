import logging
from twisted.web.resource import Resource
import json
import util


class Location(Resource):
    isLeaf = True
    template_HTML = util.tpl_lookup.get_template('location.html')

    def __init__(self, mongodb):
        Resource.__init__(self)
        self.locations = mongodb.locations
        self.users = mongodb.users

    def render_GET(self, request):
        type_key = util.get_output_type_from_request(request)
        if type_key == 'JSON':
            return self.render_JSON(request)
        else:  # type_key == 'HTML'
            return self.render_HTML(request)

    def render_HTML(self, request):
        try:
            user = self.get_user(request)
            location = self.get_location(user)
            data = {'location': location, 'user': user}
        except UserWarning:
            data = {'errno': 11, 'error': 'Not logged in!'}
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return self.template_HTML.render(**data).encode('utf-8')

    def render_JSON(self, request):
        try:
            user = self.get_user(request)
            location = self.get_location(user)
            data = {'location': location}
        except UserWarning:
            data = {'errno': 11, 'error': 'Not logged in!'}
        request.setHeader("Content-Type", "text/plain; charset=utf-8")
        return json.dumps(data).encode('utf-8')

    def get_user(self, request):
        login = util.User(request.getSession()).login
        if login is None:
            logging.warn('User not logged in!')
            raise UserWarning('Not logged in!')
        logging.debug('Logged user: %s', login)
        return self.users.find_one({'login': login})

    def get_location(self, user):
        return self.locations.find_one({'_id': user['location_id']})
