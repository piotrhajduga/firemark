import logging

from django.core.exceptions import PermissionDenied
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import models, serializers, permissions

# Create your views here.
log = logging.getLogger(__name__)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationSerializer
    permission_classes = (IsAuthenticated, permissions.HasLocationAccess,)

    def get_queryset(self):
        return models.Location.objects.filter(
            Q(owner=self.request.user.creator) | Q(public=True)
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.creator)


class LocationExitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationExitSerializer
    permission_classes = (IsAuthenticated, permissions.HasLocationExitAccess,)

    def get_queryset(self):
        return models.LocationExit.objects.filter(
            source__owner=self.request.user.creator
        )

    def perform_create(self, serializer):
        source = models.Location.objects.get(id=serializer.data['source'])
        if source.owner.user != self.request.user:
            raise PermissionDenied(
                'Only source location owner can create'
                'exits for the source location'
            )
        serializer.save()

    def perform_update(self, serializer):
        source = models.Location.objects.get(id=serializer.data['source'])
        if source.owner.user != self.request.user:
            raise PermissionDenied(
                'Only source location owner can update'
                'exits for the source location'
            )
        serializer.save()


class LocationItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationItemSerializer
    permission_classes = (IsAuthenticated, permissions.HasLocationItemAccess,)

    def get_queryset(self):
        return models.LocationItem.objects.filter(
            location__owner=self.request.user.creator
        ).order_by('order')

    def perform_create(self, serializer):
        source = models.Location.objects.get(id=serializer.data['location'])
        if source.owner.user != self.request.user:
            raise PermissionDenied(
                'Only location owner can create items for the location'
            )
        serializer.save()

    def perform_update(self, serializer):
        source = models.Location.objects.get(id=serializer.data['location'])
        if source.owner.user != self.request.user:
            raise PermissionDenied(
                'Only location owner can update items for the location'
            )
        serializer.save()
