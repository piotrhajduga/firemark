from django.views.generic import TemplateView, DetailView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from locations.models import LocationItem
from .models import ActorPlayer
from .serializers import GameStateSerializer


# Create your views here.


class GameAPIView(generics.RetrieveUpdateAPIView):
    queryset = ActorPlayer.objects.all()
    serializer_class = GameStateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset.get(user=self.request.user)


class GameView(TemplateView):
    template_name = "index.html"

    @property
    def extra_context(self):
        return {
            "title": "Firemark"
        }

class GameMainWidgetView(TemplateView):
    template_name = "main_widget.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            player = ActorPlayer.objects.get(user=self.request.user)
            context['location'] = player.location
        return context