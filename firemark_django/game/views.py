from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import ActorPlayer
from .permissions import IsActorPlayer
from .serializers import GameStateSerializer


# Create your views here.


class GameAPIView(generics.RetrieveUpdateAPIView):
    queryset = ActorPlayer.objects.all()
    serializer_class = GameStateSerializer
    permission_classes = [IsAuthenticated, IsActorPlayer]

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        return queryset.get(user=self.request.user)
