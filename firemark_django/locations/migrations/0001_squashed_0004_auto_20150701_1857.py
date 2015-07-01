# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('locations', '0001_initial'), ('locations', '0002_auto_20150701_1848'), ('locations', '0003_auto_20150701_1856'), ('locations', '0004_auto_20150701_1857')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorCreator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('codename', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('allow_portals', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(related_name='locations', to='locations.ActorCreator')),
            ],
            options={
                'db_tablespace': 'locations_ts',
            },
        ),
        migrations.CreateModel(
            name='LocationExit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('codename', models.CharField(max_length=255)),
                ('destination', models.ForeignKey(related_name='entrances', to='locations.Location')),
                ('source', models.ForeignKey(related_name='exits', to='locations.Location')),
            ],
            options={
                'db_tablespace': 'locations_ts',
            },
        ),
        migrations.CreateModel(
            name='LocationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('version', models.CharField(max_length=255, null=True)),
                ('order', models.IntegerField()),
                ('config', models.TextField()),
                ('location', models.ForeignKey(related_name='items', to='locations.Location')),
            ],
            options={
                'db_tablespace': 'locations_ts',
            },
        ),
        migrations.CreateModel(
            name='LocationItemType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('codename', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('enabled', models.BooleanField()),
                ('config_schema', models.TextField()),
            ],
            options={
                'db_tablespace': 'locations_ts',
            },
        ),
        migrations.AlterUniqueTogether(
            name='locationitemtype',
            unique_together=set([('codename', 'version')]),
        ),
        migrations.AddField(
            model_name='locationitem',
            name='type',
            field=models.ForeignKey(related_name='+', to='locations.LocationItemType'),
        ),
        migrations.AlterUniqueTogether(
            name='locationexit',
            unique_together=set([('source', 'destination', 'codename')]),
        ),
        migrations.AlterIndexTogether(
            name='locationexit',
            index_together=set([('source', 'codename'), ('source', 'destination')]),
        ),
        migrations.RenameField(
            model_name='location',
            old_name='allow_portals',
            new_name='public',
        ),
    ]
