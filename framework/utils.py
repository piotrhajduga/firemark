from pyramid.config import Configurator
from api import routes


def get_router():
    router = Configurator()
    router.add_static_view('/', '../webapp')
    for route_name, url in routes:
        router.add_route(route_name, url)
    return router
