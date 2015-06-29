from rest_framework import viewsets
from . import models, serializers, permissions

# Create your views here.


class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
    permission_classes = (permissions.IsLocationOwner,)
