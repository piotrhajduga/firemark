import logging
from twisted.web.resource import Resource
from exc import NotLoggedIn, InsufficientPriviledges
import json
import util


def checkBuilderPriviledges(user):
    if user is None:
        raise NotLoggedIn()
    elif 'builder' not in user.get_roles():
        raise InsufficientPriviledges()


class LocationSearch(Resource):
    def __init__(self, location_service):
        self.locs = location_service

    def render_POST(self, request):
        try:
            session = util.Session(request.getSession())
            checkBuilderPriviledges(session.user)
            word = str(request.args['LocationSearch'][0])
            locations = self.locs.search(name_like=word)
            return json.dumps({'locations': locations,
                               'errno': 0, 'error': 'OK'})
        except UserWarning as exc:
            logging.exception('Exception during location search')
            return json.dumps({'errno': exc.errno, 'error': ''})


class LocationEdit(Resource):
    def __init__(self, location_service):
        self.locs = location_service

    def render_POST(self, request):
        session = util.Session(request.getSession())
        checkBuilderPriviledges(session.user)


class Builder(Resource):
    def __init__(self, location_service):
        Resource.__init__(self)
        self.putChild('searchlocation', LocationSearch(location_service))
