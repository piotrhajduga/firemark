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
    permission_classes = [IsAuthenticated, permissions.HasLocationAccess,]

    def get_queryset(self):
        return models.Location.objects.filter(
            Q(owner=self.request.user.creator) | Q(public=True)
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.creator)