from django.conf.urls import include, url

from game.urls import urlpatterns as game_urls
from locations.urls import urlpatterns as locations_urls

urlpatterns = [
    url('auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(game_urls)),
    url(r'^', include(locations_urls)),
]
