# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_squashed_0004_auto_20150701_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationitem',
            name='config',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='locationitem',
            name='order',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='locationitemtype',
            name='config_schema',
            field=jsonfield.fields.JSONField(),
        ),
    ]
