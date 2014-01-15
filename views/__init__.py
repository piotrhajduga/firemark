from twisted.web.static import File
import views.rest
import views.desktop


def get_app_resource(db, config):
    resource = File('webapp/desktop')
    resource.putChild('api', views.rest.get_app_resource(db, config))
    return resource
