import logging
from twisted.web.resource import Resource
from twisted.web.error import NoResource
#from twisted.web.util import Redirect
#from twisted.web.util import urlpath
import json


class Action(Resource):
    _renderers = {}

    def __init__(self):
        Resource.__init__(self)
        self.setRenderer('JSON', json.dumps)

    def setRenderer(self, key, renderer):
        self._renderers[key] = renderer

    def render_GET(self, request):
        logging.info('GET REQUEST: %s', request)
        logging.debug('HEADERS: %s', request.getAllHeaders())
        logging.debug('GET ARGS: %s', request.args)
        try:
            try:
                type_key = str(request.args['output'][0]).upper()
            except KeyError:
                type_key = 'HTML'
            render = self._renderers[type_key]
            logging.info('Returning %s string as a result', type_key)
            return render(request.getAllHeaders())
        except KeyError:
            logging.exception('Cannot find renderer for type %s', type_key)
        return 'Cannot render data in type %s' % type_key


class Location(Action):
    def __init__(self):
        Action.__init__(self)
        self.setRenderer('HTML', self.renderHTML)

    def getChild(self, name, request):
        logging.warn('No children to this page')
        return NoResource()

    def renderHTML(self, data):
        return '<html><body></body></html>'


# actions resources resource
resources = Resource()
resources.putChild('location', Location())
