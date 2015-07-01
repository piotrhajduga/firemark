from django.db.models import Q
from rest_framework import viewsets
from . import models, serializers, permissions
import logging

# Create your views here.
log = logging.getLogger(__name__)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationSerializer
    permission_classes = (permissions.IsOwnerOrIsPublicReadOnly,)

    def get_queryset(self):
        try:
            return models.Location.objects.filter(
                Q(owner=self.request.user.creator) | Q(public=True)
            )
        except AttributeError as exc:
            log.exception(str(exc))
            return None

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.creator)


class LocationExitViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationExitSerializer
    permission_classes = (permissions.IsLocationExitOwner,)

    def get_queryset(self):
        try:
            return models.LocationExit.objects.filter(
                source__owner=self.request.user.creator
            )
        except AttributeError as exc:
            log.exception(str(exc))
            return None


class LocationItemViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationItemSerializer
    permission_classes = (permissions.IsLocationItemOwner,)

    def get_queryset(self):
        try:
            return models.LocationItem.objects.filter(
                location__owner=self.request.user.creator
            ).order_by('order')
        except AttributeError as exc:
            log.exception(str(exc))
            return None
