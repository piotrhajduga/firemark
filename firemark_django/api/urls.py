from django.urls import include, path

from game.urls import urlpatterns as game_urls
from locations.urls import urlpatterns as locations_urls

urlpatterns = [
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(game_urls)),
    path('', include(locations_urls)),
]
