#from django.core.exceptions import PermissionDenied
from rest_framework import serializers


class LocationItemSerializer(serializers.Serializer):
    codename = serializers.CharField(read_only=True)
    schema = serializers.CharField(read_only=True, source='type.game_schema')


class GameStateSerializer(serializers.Serializer):
    items = serializers.SerializerMethodField()
    action_item = serializers.CharField(write_only=True)
    action_data = serializers.CharField(write_only=True)

    def get_items(self, obj):
        return LocationItemSerializer(obj.location.items, many=True).data

    def update(self, instance, validated_data):
        #TODO
        #apply location item logics on validated_data
        #update the instance based on logics output
        return instance
