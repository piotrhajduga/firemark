from django.urls import path
from django.views.decorators.csrf import ensure_csrf_cookie

from game.views import (
    GameAPIView,
)

urlpatterns = [
    path('game/', ensure_csrf_cookie(GameAPIView.as_view())),
]
