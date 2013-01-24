import logging
from twisted.web.resource import Resource
from twisted.web.util import redirectTo
from engine.location import PlayerNotInLocation, LocationNotFound
from actions.desktop import tpl_lookup


class Location(Resource):
    isLeaf = True
    template_HTML = tpl_lookup.get_template('location.html')

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
        if errno == 11:
            session.errno, session.error = errno, error
            return redirectTo('/', request)
        return self.template_HTML.render(location)
