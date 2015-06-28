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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('active', models.BooleanField()),
                ('limit', models.IntegerField()),
                ('user_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('chmod', models.DecimalField(decimal_places=0, max_digits=3)),
                ('searchable', models.BooleanField()),
                ('owner_id', models.ForeignKey(to='locations.ActorCreator')),
            ],
        ),
        migrations.CreateModel(
            name='LocationExit',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('codename', models.CharField(max_length=255)),
                ('destination_location_id', models.ForeignKey(to='locations.Location', related_name='destination_location')),
                ('source_location_id', models.ForeignKey(to='locations.Location', related_name='source_location')),
            ],
        ),
        migrations.CreateModel(
            name='LocationItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('order', models.IntegerField()),
                ('config', models.TextField()),
                ('location_id', models.ForeignKey(to='locations.Location')),
            ],
        ),
        migrations.CreateModel(
            name='LocationItemType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('codename', models.CharField(max_length=255)),
                ('version', models.CharField(max_length=255)),
                ('enabled', models.BooleanField()),
                ('config_schema', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='locationitem',
            name='type_id',
            field=models.ForeignKey(to='locations.LocationItemType'),
        ),
    ]
