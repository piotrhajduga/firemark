from twisted.web.static import File
import views.rest
import views.desktop


def get_app_resource(db, config):
    resource = views.desktop.get_app_resource(db, config)
    resource.putChild('static', File('static/desktop'))
    resource.putChild('json', views.rest.get_app_resource(db, config))
    return resource
