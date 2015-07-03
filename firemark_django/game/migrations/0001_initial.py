# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20150703_2124'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorPlayer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('active', models.BooleanField(default=True)),
                ('location', models.ForeignKey(to='locations.Location', related_name='+')),
                ('user', models.OneToOneField(related_name='player', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_tablespace': 'game_ts',
            },
        ),
    ]
