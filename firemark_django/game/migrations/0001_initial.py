# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorPlayer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('location', models.ForeignKey(related_name='+', to='locations.Location')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='player')),
            ],
            options={
                'db_tablespace': 'game_ts',
            },
        ),
    ]
