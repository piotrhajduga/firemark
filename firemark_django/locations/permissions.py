from rest_framework import permissions


class HasLocationAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.request.is_authenticated() and (
            obj.public and request.method in permissions.SAFE_METHODS
            or obj.owner == request.user.creator
        )


class HasLocationExitAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.request.is_authenticated() and (
            obj.source.public and request.method in permissions.SAFE_METHODS
            or obj.source.owner == request.user.creator
        )


class HasLocationItemAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return self.request.is_authenticated() and (
            obj.source.public and request.method in permissions.SAFE_METHODS
            or obj.location.owner == request.user.creator
        )
