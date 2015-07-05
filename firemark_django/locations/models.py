from django.db import models
from django.contrib.auth.models import User

LOCATIONS_TABLESPACE = 'locations_ts'


# Create your models here.


class ActorCreator(models.Model):
    user = models.OneToOneField(User, related_name="creator")
    active = models.BooleanField(default=False)
    limit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '{0}(creator)'.format(self.user)


class Location(models.Model):
    owner = models.ForeignKey(ActorCreator, related_name="locations")
    codename = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, blank=True)
    public = models.BooleanField(default=False)

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE

    def __str__(self):
        return str(self.codename)


class LocationExit(models.Model):
    source = models.ForeignKey(Location, related_name="exits")
    destination = models.ForeignKey(Location, related_name="entrances")
    codename = models.CharField(max_length=255)

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE
        unique_together = (
            ('source', 'destination'),
            ('source', 'codename'),
        )
        index_together = (
            ('source', 'destination'),
            ('source', 'codename'),
        )

    def __str__(self):
        return "{0}({1}->{2})".format(
            self.codename, self.source, self.destination)


class LocationItem(models.Model):
    location = models.ForeignKey(Location, related_name="items")
    codename = models.CharField(max_length=32)
    type = models.CharField(max_length=255)
    order = models.IntegerField(null=True)
    config = models.TextField()

    class Meta:
        db_tablespace = LOCATIONS_TABLESPACE
        unique_together = ('location', 'codename')
        index_together = ('location', 'codename')

    def __str__(self):
        return 'Item {0}({1})'.format(self.type, self.location)
