from rest_framework import viewsets
from . import models, serializers

# Create your views here.


class LocationViewSet(viewsets.ModelViewSet):
    queryset = models.Location.objects.all()
    serializer_class = serializers.LocationSerializer
