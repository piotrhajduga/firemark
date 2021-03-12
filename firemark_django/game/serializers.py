import json
from jsonspec.validators import load, ValidationError
#from django.core.exceptions import PermissionDenied
from rest_framework import serializers
from locations.item_types import ItemType


class LocationItemSerializer(serializers.Serializer):
    codename = serializers.CharField(read_only=True)
    data = serializers.SerializerMethodField()
    type = serializers.CharField(read_only=True)
    schema = serializers.SerializerMethodField()

    def get_data(self, obj):
        ''' Get data to be displayed based on location item config '''
        instance = ItemType.get_instance(obj)
        return instance.get_data()

    def get_schema(self, obj):
        ''' Get schema for the input based on location item type '''
        instance = ItemType.get_instance(obj)
        return instance.get_game_schema()


class GameStateSerializer(serializers.Serializer):
    items = serializers.SerializerMethodField()
    action_item = serializers.CharField(write_only=True)
    action_data = serializers.CharField(write_only=True)

    def get_items(self, obj):
        return LocationItemSerializer(obj.location.items, many=True).data

    def validate(self, data):
        item = self.get_location_item(data['action_item'])
        if not item:
            raise serializers.ValidationError(
                'Action item "{0}"'
                'could not be found'.format(data['action_item'])
            )
        item_type = ItemType.get_instance(item)
        try:
            action_data = json.loads(data['action_data'])
            json_validator = load(item_type.get_game_schema())
            json_validator.validate(action_data)
            return {
                'item_type': item_type,
                'action_item': data['action_item'],
                'action_data': action_data,
            }
        except ValueError as exc:
            raise serializers.ValidationError(exc)
        except ValidationError as exc:
            raise serializers.ValidationError(exc)

    def update(self, instance, validated_data):
        #apply location item logics on validated_data
        #update the instance based on logics output
        item_type = validated_data['item_type']
        item_type.process(instance, validated_data['action_data'])
        return instance

    #TODO: set up caching for this method
    def get_location_item(self, codename):
        return self.instance.location.items.get(codename=codename)
