from django.db import models
from django.contrib.auth.models import User
import uuid

LOCATIONS_TABLESPACE = 'locations_ts'


# Create your models here.


class ActorCreator(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, related_name="creator")

    def __str__(self):
        return '{0}(creator)'.format(self.user)


class Location(models.Model):
    id = models.CharField(max_length=40, primary_key=True, default=uuid.uuid4)
    owner = models.ForeignKey(ActorCreator, on_delete=models.DO_NOTHING, related_name="locations")
    codename = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, blank=True)
    public = models.BooleanField(default=False)

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE

    def __str__(self):
        return str(self.codename)


class LocationItem(models.Model):
    id = models.CharField(max_length=40, primary_key=True, default=uuid.uuid4)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="items")
    type = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    config = models.TextField()

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE

    def __str__(self):
        return 'Item {0}({1})'.format(self.type, self.location)
