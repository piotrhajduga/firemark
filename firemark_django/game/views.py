from django.core.exceptions import PermissionDenied
from rest_framework import generics
from .models import ActorPlayer
from .serializers import GameStateSerializer

# Create your views here.


class GameAPIView(generics.RetrieveUpdateAPIView):
    queryset = ActorPlayer.objects.all()
    serializer_class = GameStateSerializer

    def get_object(self):
        if not self.request.user.is_authenticated():
            raise PermissionDenied(
                'Only authenticated player users can access the game'
            )
        queryset = self.filter_queryset(self.get_queryset())
        return queryset.get(user=self.request.user)
