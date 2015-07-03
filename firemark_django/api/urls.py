from django.conf.urls import include, url
from locations.urls import urlpatterns as locations_urls
from game.views import (
    GameAPIView,
)

urlpatterns = [
    url(r'^', include(locations_urls)),
    url(r'^game/', GameAPIView.as_view()),
]
