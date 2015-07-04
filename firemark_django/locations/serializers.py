from rest_framework import serializers
from . import models


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = (
            'id', 'owner', 'codename', 'tags',
            'public', 'exits', 'entrances', 'items'
        )
        read_only_fields = ('owner',)


class LocationExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocationExit
        fields = ('id', 'codename', 'source', 'destination')


class LocationItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocationItem
        fields = ('id', 'location', 'type', 'order', 'config')
        read_only_fields = ('version',)
