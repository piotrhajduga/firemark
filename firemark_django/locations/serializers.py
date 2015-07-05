import json
from jsonspec.validators import load, ValidationError
from rest_framework import serializers
from . import models, item_types


class LocationExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LocationExit
        fields = ('codename', 'source', 'destination')


class LocationItemSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=item_types.get_type_choices())

    class Meta:
        model = models.LocationItem
        fields = ('location', 'codename', 'type', 'order', 'config')

    def validate_config(self, value):
        try:
            value_json = json.loads(value)
            cls = item_types.ItemType.get_class(self.initial_data['type'])
            json_validator = load(cls.config_schema)
            json_validator.validate(value_json)
            return json.dumps(value_json)
        except ValueError as exc:
            raise serializers.ValidationError(exc)
        except ValidationError as exc:
            raise serializers.ValidationError(exc)


class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(source='owner.user')
    items = serializers.SerializerMethodField()
    exits = serializers.SerializerMethodField()
    entrances = serializers.SerializerMethodField()

    class Meta:
        model = models.Location
        fields = (
            'id', 'owner', 'codename', 'tags',
            'public', 'exits', 'entrances', 'items'
        )
        read_only_fields = ('owner', 'exits', 'entrances', 'items')

    def get_items(self, obj):
        return ROLocationItemSerializer(obj.items, many=True).data

    def get_exits(self, obj):
        return ROLocationExitSerializer(obj.exits, many=True).data

    def get_entrances(self, obj):
        return ROLocationEntranceSerializer(obj.entrances, many=True).data


class ROLocationItemSerializer(serializers.Serializer):
    type = serializers.CharField(read_only=True)
    codename = serializers.CharField(read_only=True)
    order = serializers.IntegerField(read_only=True)
    config = serializers.SerializerMethodField()

    def get_config(self, obj):
        return json.loads(obj.config)


class ROLocationExitSerializer(serializers.Serializer):
    codename = serializers.CharField(read_only=True)
    destination = serializers.StringRelatedField(read_only=True)


class ROLocationEntranceSerializer(serializers.Serializer):
    codename = serializers.CharField(read_only=True)
    source = serializers.StringRelatedField(read_only=True)
