# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_zoom_world', '0002_auto_20151106_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='property_access',
            field=models.ManyToManyField(to='a_zoom_world.AccessibilityNeed'),
        ),
    ]
