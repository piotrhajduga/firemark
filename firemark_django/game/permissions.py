from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from game.models import ActorPlayer


class IsActorPlayer(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            ActorPlayer.objects.get(user = request.user)
            return True
        except ObjectDoesNotExist:
            return False