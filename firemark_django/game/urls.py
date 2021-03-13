from django.conf.urls import include, url
from django.urls import path

from locations.urls import urlpatterns as locations_urls
from game.views import (
    GameView, GameMainWidgetView,
)

urlpatterns = [
    path('main', GameMainWidgetView.as_view()),
    path('', GameView.as_view()),
]
