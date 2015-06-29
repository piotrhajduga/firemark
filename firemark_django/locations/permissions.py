from rest_framework import permissions
from .models import ActorCreator


class IsLocationOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == ActorCreator.objects.get(user=request.user)
