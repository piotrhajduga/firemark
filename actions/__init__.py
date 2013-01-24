from twisted.web.resource import Resource
from twisted.web.static import File
import actions.json
import actions.desktop


def get_app_resource(db, config):
    resource = actions.desktop.get_app_resource(db, config)
    resource.putChild('static', File('static/desktop'))
    resource.putChild('json', actions.json.get_app_resource(db, config))
    return resource
