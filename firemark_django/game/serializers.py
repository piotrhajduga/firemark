#from django.core.exceptions import PermissionDenied
from rest_framework import serializers


class LocationItemSerializer(serializers.Serializer):
    codename = serializers.CharField(read_only=True)
    data = serializers.SerializerMethodField()
    type = serializers.CharField(read_only=True)
    schema = serializers.SerializerMethodField()

    def get_data(self, obj):
        ''' Get data to be displayed based on location item config '''
        return {}

    def get_schema(self, obj):
        ''' Get schema for the input based on location item type '''
        return {}


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
