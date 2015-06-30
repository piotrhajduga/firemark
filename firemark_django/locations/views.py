from rest_framework import viewsets
from . import models, serializers, permissions
import logging

# Create your views here.
log = logging.getLogger(__name__)


class LocationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.LocationSerializer
    permission_classes = (permissions.IsLocationOwner,)

    def get_queryset(self):
        try:
            return models.Location.objects.filter(
                owner=self.request.user.creator)
        except AttributeError as exc:
            log.exception(str(exc))
            return None

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.creator)
