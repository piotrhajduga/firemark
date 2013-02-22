import logging
from twisted.web.resource import Resource
from twisted.web.util import redirectTo, Redirect
from meta import tpl_lookup
from util import Session


class Builder(Resource):
    template_HTML = tpl_lookup.get_template('builder.html')

    def __init__(self, location_service):
        Resource.__init__(self)
        self.putChild('', Redirect('/'))

    def render_GET(self, request):
        session = Session(request.getSession())
        errno, error = 0, 'OK'
        if session.user is None:
            logging.warn('User not logged in!')
            errno, error = 11, 'Not logged in!'
        elif 'builder' not in session.user['roles']:
            logging.warn('User is not a builder!')
            errno, error = 18, 'Access denied!'
        if errno:
            session.errno, session.error = errno, error
            return redirectTo('/', request)
        return self.template_HTML.render()
