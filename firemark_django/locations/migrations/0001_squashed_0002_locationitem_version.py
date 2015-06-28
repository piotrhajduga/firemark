# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [('locations', '0001_initial'), ('locations', '0002_locationitem_version')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorCreator',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('active', models.BooleanField()),
                ('limit', models.IntegerField()),
                ('user_id', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tags', models.CharField(max_length=255)),
                ('chmod', models.DecimalField(max_digits=3, decimal_places=0)),
                ('searchable', models.BooleanField()),
                ('owner_id', models.ForeignKey(to='locations.ActorCreator')),
            ],
        ),
        migrations.CreateModel(
            name='LocationExit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('codename', models.CharField(max_length=255)),
                ('destination_location_id', models.ForeignKey(related_name='destination_location', to='locations.Location')),
                ('source_location_id', models.ForeignKey(related_name='source_location', to='locations.Location')),
            ],
        ),
        migrations.CreateModel(
            name='LocationItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('config', models.TextField()),
                ('location_id', models.ForeignKey(to='locations.Location')),
            ],
        ),
        migrations.CreateModel(
            name='LocationItemType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
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
        migrations.AddField(
            model_name='locationitem',
            name='version',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
