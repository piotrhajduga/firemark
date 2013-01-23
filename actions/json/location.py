import logging
from twisted.web.resource import Resource
import json
import util
from engine.location import PlayerNotInLocation, LocationNotFound


class Location(Resource):
    isLeaf = True

    def __init__(self, locationservice):
        Resource.__init__(self)
        self.locs = locationservice

    def render_GET(self, request):
        session = util.Session(request.getSession())
        errno, error = 0, 'OK'
        try:
            if session.user is None:
                raise UserWarning('Not logged in!')
            location = self.locs.get_for_user(session.user['_id'])
        except UserWarning:
            logging.warn('User not logged in!')
            errno, error = 11, 'Not logged in!'
        except PlayerNotInLocation:
            logging.warn('User is not in location')
            errno, error = 16, 'User is not in location'
            location = self.locs.get_starting_location()
        except LocationNotFound:
            logging.error('Location not found')
            errno, error = 17, 'Location not found'
            location = self.locs.get_starting_location()
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        return json.dumps({'location': location, 'errno': errno, 'error': error})
