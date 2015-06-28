from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ActorCreator(models.Model):
    user_id = models.OneToOneField(User)
    active = models.BooleanField()
    limit = models.IntegerField()


class Location(models.Model):
    owner_id = models.ForeignKey(ActorCreator)
    name = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    chmod = models.DecimalField(max_digits=3, decimal_places=0)
    searchable = models.BooleanField()


class LocationExit(models.Model):
    source_location_id = models.ForeignKey(
        Location, related_name="source_location")
    destination_location_id = models.ForeignKey(
        Location, related_name="destination_location")
    codename = models.CharField(max_length=255)


class LocationItemType(models.Model):
    codename = models.CharField(max_length=255)
    version = models.CharField(max_length=255, null=False)
    enabled = models.BooleanField()
    config_schema = models.TextField()


class LocationItem(models.Model):
    type_id = models.ForeignKey(LocationItemType)
    version = models.CharField(max_length=255, null=True)
    location_id = models.ForeignKey(Location)
    order = models.IntegerField()
    config = models.TextField()
