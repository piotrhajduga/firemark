from django.urls import path

from .views import (
    GameView, GameMainWidgetView,
)

urlpatterns = [
    path('main', GameMainWidgetView.as_view()),
    path('', GameView.as_view()),
]
