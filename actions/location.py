import logging
from twisted.web.resource import Resource
from twisted.web.util import redirectTo
import json
import util
from engine.locationservice import UserNotInLocation, LocationNotFound


class Location(Resource):
    isLeaf = True
    template_HTML = util.tpl_lookup.get_template('location.html')

    def __init__(self, locationservice):
        Resource.__init__(self)
        self.locs = locationservice

    def render_GET(self, request):
        type_key = util.get_output_type_from_request(request)
        session = util.Session(request.getSession())
        errno, error = 0, None
        try:
            if session.user is None:
                raise UserWarning('Not logged in!')
            location = self.locs.get_for_user(session.user['_id'])
        except UserWarning:
            logging.warn('User not logged in!')
            errno, error = 11, 'Not logged in!'
        except UserNotInLocation:
            logging.warn('User is not in location')
            errno, error = 16, 'User is not in location'
            location = self.locs.get_starting_location()
        except LocationNotFound:
            logging.error('Location not found')
            errno, error = 17, 'Location not found'
            location = self.locs.get_starting_location()
        request.setHeader("Content-Type", "text/html; charset=utf-8")
        if type_key == 'JSON':
            if errno:
                return json.dumps({'errno': errno, 'error': error})
            return json.dumps(location)
        # type_key == 'HTML'
        session.errno, session.error = errno, error
        if errno == 11:
            return redirectTo('/', request)
        return self.template_HTML.render(**location)
