# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amenity',
            name='property_amenity',
        ),
        migrations.RemoveField(
            model_name='exceptions',
            name='property_need',
        ),
        migrations.RemoveField(
            model_name='potentialallergen',
            name='property_allergens',
        ),
        migrations.AddField(
            model_name='amenity',
            name='type',
            field=models.CharField(default=None, max_length=500),
        ),
        migrations.AddField(
            model_name='property',
            name='property_allergens',
            field=models.ManyToManyField(to='property.PotentialAllergen'),
        ),
        migrations.AddField(
            model_name='property',
            name='property_amenity',
            field=models.ManyToManyField(to='property.Amenity'),
        ),
        migrations.AddField(
            model_name='propertyneed',
            name='property_need',
            field=models.ManyToManyField(to='property.Exceptions'),
        ),
    ]
