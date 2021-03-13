from django.conf.urls import include, url
from django.urls import path

from locations.urls import urlpatterns as locations_urls
from game.views import (
    GameAPIView,
)

urlpatterns = [
    path('game/', GameAPIView.as_view()),
    url(r'', include(locations_urls)),
]
