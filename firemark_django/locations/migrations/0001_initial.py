# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

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
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='creator')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('codename', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('allow_portals', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(to='locations.ActorCreator', related_name='locations')),
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
                ('destination', models.ForeignKey(to='locations.Location', related_name='entrances')),
                ('source', models.ForeignKey(to='locations.Location', related_name='exits')),
            ],
            options={
                'db_tablespace': 'locations_ts',
            },
        ),
        migrations.CreateModel(
            name='LocationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('version', models.CharField(null=True, max_length=255)),
                ('order', models.IntegerField()),
                ('config', models.TextField()),
                ('location', models.ForeignKey(to='locations.Location', related_name='items')),
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
            name='loctype',
            field=models.ForeignKey(to='locations.LocationItemType'),
        ),
        migrations.AlterUniqueTogether(
            name='locationexit',
            unique_together=set([('source', 'destination', 'codename')]),
        ),
        migrations.AlterIndexTogether(
            name='locationexit',
            index_together=set([('source', 'destination'), ('source', 'codename')]),
        ),
    ]
