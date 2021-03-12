from django.conf.urls import include, url
from locations.urls import urlpatterns as locations_urls
from game.views import (
    GameView, GameMainWidgetView,
)

urlpatterns = [
    url('main', GameMainWidgetView.as_view()),
    url('', GameView.as_view()),
]
