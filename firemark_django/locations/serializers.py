import json

from jsonspec.validators import load, ValidationError
from rest_framework import serializers

from . import models, item_types
from .models import LocationItem, Location


class LocationItemConfigSerializer(serializers.Serializer):
    def to_representation(self, instance):
        return json.loads(instance)

    def to_internal_value(self, data):
        return json.dumps(data)

def validate_item_config(value, item_type):
    try:
        value_json = json.loads(value)
        cls = item_types.ItemType.get_class(item_type)
        json_validator = load(cls.config_schema)
        json_validator.validate(value_json)
        return value
    except ValueError as exc:
        raise serializers.ValidationError(exc)
    except ValidationError as exc:
        raise serializers.ValidationError("Config value must be valid with item type schema")


class LocationItemSerializer(serializers.ModelSerializer):
    type = serializers.ChoiceField(choices=item_types.get_type_choices())
    order = serializers.IntegerField(allow_null=True, required=False)
    config = LocationItemConfigSerializer()

    class Meta:
        model = models.LocationItem
        fields = ('id', 'type', 'order', 'config')
        read_only_fields = ('id',)


class LocationSerializer(serializers.ModelSerializer):
    items = LocationItemSerializer(many=True)

    class Meta:
        model = models.Location
        exclude = ['owner']
        read_only_fields = ['id']
        depth = 2

    def create(self, validated_data):
        data = {
            k:v for (k,v)
            in validated_data.items()
            if k in ["codename", "tags", "public", "owner"]
        }
        location = Location.objects.create(**data)
        for item in validated_data["items"]:
            validate_item_config(item["config"], item["type"])
            LocationItem.objects.create(location=location, **item)
        return location

    def update(self, instance, validated_data):
        instance.codename = validated_data["codename"]
        instance.tags = validated_data["tags"]
        instance.public = validated_data["public"]
        instance.save()
        LocationItem.objects.filter(location=instance).delete()
        for item in validated_data["items"]:
            validate_item_config(item["config"], item["type"])
            LocationItem.objects.create(location=instance, **item)
        return instance