from django.db.models import Q
from django.core.exceptions import PermissionDenied
from rest_framework import viewsets
from . import models, serializers, permissions
import logging

# Create your views here.
log = logging.getLogger(__name__)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationSerializer
    permission_classes = (permissions.HasLocationAccess,)

    def get_queryset(self):
        try:
            return models.Location.objects.filter(
                Q(owner=self.request.user.creator) | Q(public=True)
            )
        except AttributeError as exc:
            log.debug(str(exc))
            raise PermissionDenied(
                'Only authenticated users can access locations'
            )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.creator)


class LocationExitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationExitSerializer
    permission_classes = (permissions.HasLocationExitAccess,)

    def get_queryset(self):
        try:
            return models.LocationExit.objects.filter(
                source__owner=self.request.user.creator
            )
        except AttributeError as exc:
            log.debug(str(exc))
            raise PermissionDenied(
                'Only authenticated users can access location exits'
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
    permission_classes = (permissions.HasLocationItemAccess,)

    def get_queryset(self):
        try:
            return models.LocationItem.objects.filter(
                location__owner=self.request.user.creator
            ).order_by('order')
        except AttributeError as exc:
            log.debug(str(exc))
            raise PermissionDenied(
                'Only authenticated users can access location items'
            )

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
