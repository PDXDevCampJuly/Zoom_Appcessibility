# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_zoom_world', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='property_id',
        ),
        migrations.AddField(
            model_name='property',
            name='property_vehicle',
            field=models.ManyToManyField(to='a_zoom_world.Vehicle'),
        ),
    ]
