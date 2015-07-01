from rest_framework import permissions


class IsOwnerOrIsPublicReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.public and request.method in permissions.SAFE_METHODS
            or obj.owner == request.user.creator
        )


class IsLocationExitOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.source.owner == request.user.creator


class IsLocationItemOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.location.owner == request.user.creator
