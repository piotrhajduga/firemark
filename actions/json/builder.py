import logging
from twisted.web.resource import Resource
import json
import util


class Builder(Resource):
    def __init__(self, location_service):
        Resource.__init__(self)
        self.putChild('searchlocation', LocationSearch(location_service))


class LocationSearch(Resource):
    def __init__(self, location_service):
        self.locs = location_service

    def render_POST(self, request):
        session = util.Session(request.getSession())
        errno, error = 0, 'OK'
        locations = []
        if session.user is None:
            logging.warn('User not logged in!')
            errno, error = 11, 'Not logged in!'
        elif 'builder' not in session.user.get_roles():
            logging.warn('User is not a builder!')
            errno, error = 18, 'Access denied!'
        if not errno:
            word = str(request.args['LocationSearch'][0])
            locations = self.locs.get_for_tag(word)
        return json.dumps({'locations': locations,
                           'errno': errno, 'error': error})
