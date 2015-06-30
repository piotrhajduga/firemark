from rest_framework import serializers
from . import models


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('id', 'owner', 'codename', 'tags', 'allow_portals')
        read_only_fields = ('owner',)
