from django.urls import path

from game.views import (
    GameAPIView,
)

urlpatterns = [
    path('game/', GameAPIView.as_view()),
]
