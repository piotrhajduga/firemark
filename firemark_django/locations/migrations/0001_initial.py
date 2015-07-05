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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('active', models.BooleanField(default=False)),
                ('limit', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(related_name='creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('codename', models.CharField(max_length=255)),
                ('tags', models.CharField(blank=True, max_length=255)),
                ('public', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(related_name='locations', to='locations.ActorCreator')),
            ],
            options={
                'db_tablespace': 'locations_ts',
            },
        ),
        migrations.CreateModel(
            name='LocationExit',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('codename', models.UUIDField(editable=False)),
                ('type', models.CharField(max_length=255)),
                ('order', models.IntegerField(null=True)),
                ('config', models.TextField()),
                ('location', models.ForeignKey(related_name='items', to='locations.Location')),
            ],
            options={
                'db_tablespace': 'locations_ts',
            },
        ),
        migrations.AlterUniqueTogether(
            name='locationitem',
            unique_together=set([('location', 'codename')]),
        ),
        migrations.AlterIndexTogether(
            name='locationitem',
            index_together=set([('location', 'codename')]),
        ),
        migrations.AlterUniqueTogether(
            name='locationexit',
            unique_together=set([('source', 'destination'), ('source', 'codename')]),
        ),
        migrations.AlterIndexTogether(
            name='locationexit',
            index_together=set([('source', 'destination'), ('source', 'codename')]),
        ),
    ]
