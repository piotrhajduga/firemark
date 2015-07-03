# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20150702_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationitemtype',
            name='game_schema',
            field=models.TextField(default='default'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='locationitem',
            name='config',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='locationitemtype',
            name='config_schema',
            field=models.TextField(),
        ),
        migrations.AlterUniqueTogether(
            name='locationexit',
            unique_together=set([('source', 'destination'), ('source', 'codename')]),
        ),
    ]
