from django.db import models
from django.contrib.auth.models import User
from locations.models import Location

GAME_TABLESPACE = 'game_ts'
# Create your models here.


class ActorPlayer(models.Model):
    user = models.OneToOneField(User, related_name="player")
    active = models.BooleanField(default=True)
    location = models.ForeignKey(Location, related_name="+")

    class Meta:
        db_tablespace = GAME_TABLESPACE

    def __str__(self):
        return '{0}(player)'.format(self.user)
