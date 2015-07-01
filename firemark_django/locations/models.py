from django.db import models
from django.contrib.auth.models import User

# Create your models here.
LOCATIONS_TABLESPACE = 'locations_ts'


class ActorCreator(models.Model):
    user = models.OneToOneField(User, related_name="creator")
    active = models.BooleanField(default=False)
    limit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{0}(creator)'.format(self.user)


class Location(models.Model):
    owner = models.ForeignKey(ActorCreator, related_name="locations")
    codename = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    public = models.BooleanField(default=False)

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE

    def __str__(self):
        return "{0}({1})".format(self.codename, self.id)


class LocationExit(models.Model):
    source = models.ForeignKey(Location, related_name="exits")
    destination = models.ForeignKey(Location, related_name="entrances")
    codename = models.CharField(max_length=255)

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE
        unique_together = (
            ('source', 'destination', 'codename'),
        )
        index_together = (
            ('source', 'destination'),
            ('source', 'codename'),
        )


class LocationItemType(models.Model):
    codename = models.CharField(max_length=255)
    version = models.CharField(max_length=255, null=False)
    enabled = models.BooleanField()
    config_schema = models.TextField()

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE
        unique_together = (
            ('codename', 'version'),
        )


class LocationItem(models.Model):
    location = models.ForeignKey(Location, related_name="items")
    type = models.ForeignKey(LocationItemType, related_name="+")
    version = models.CharField(max_length=255, null=True)
    order = models.IntegerField()
    config = models.TextField()

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE
