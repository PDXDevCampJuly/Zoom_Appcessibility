# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import json
from django.db import migrations
from a_zoom_world.models import DomicileType, Amenity, PotentialAllergen, \
    AccessibilityNeed


def load_potential_allergen(apps, schema_editor):
    # this function loads a json file to make it easily editable as a python object
    with open('a_zoom_world/static/json/potential_allergen.json') as json_file:
        json_data = json.load(json_file)

    for allergy in json_data:
        # loop through the jason data and add to potential allergen table
        pa = PotentialAllergen(description=allergy['allergy'])
        # this saves to the database
        pa.save()


def load_service_amenties(apps, schema_editor):
    with open('a_zoom_world/static/json/service_amenities.json') as json_file:
        json_data = json.load(json_file)

    for amenity in json_data:
        sa = Amenity(type=amenity['amenity'])
        sa.save()


def load_domicile_type(apps, schema_editor):
    with open('a_zoom_world/static/json/domicile_type') as json_file:
        json_data = json.load(json_file)

    for domicile in json_data:
        dt = DomicileType(type=domicile['domicile'])
        dt.save()


def load_accessibility_needs(apps, schema_editor):
    with open('a_zoom_world/static/json/accessibility_needs.json') as json_file:
        json_data = json.load(json_file)

    for accessibilityneed in json_data:
        pn = AccessibilityNeed(name=accessibilityneed['accessneed'],
                               description=accessibilityneed['description'])
        pn.save()


def reverse_func():
    # A dummy function so the zero works.
    pass


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessibilityNeed',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200, default=None)),
                ('description', models.CharField(max_length=1000, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('street', models.CharField(max_length=200, default=None)),
                ('street_two', models.CharField(max_length=200, blank=True)),
                ('city', models.CharField(max_length=50, default=None)),
                ('state', models.CharField(max_length=50, default=None)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=500, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='DomicileType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('type', models.CharField(max_length=500, default=None)),
                ('square_feet', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='NeedException',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('need', models.CharField(max_length=200, default=None)),
                ('room_location', models.CharField(max_length=200, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='PotentialAllergen',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.CharField(max_length=500, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50, default=None)),
                ('description', models.CharField(max_length=2000, default=None)),
                ('num_bedroom', models.CharField(max_length=20, default=None)),
                ('num_bathroom', models.CharField(max_length=20, default=None)),
                ('access_num_bedroom', models.CharField(max_length=20, default=None)),
                ('access_num_bathroom', models.CharField(max_length=20, default=None)),
                ('address', models.ForeignKey(to='a_zoom_world.Address')),
                ('photo_property', models.ManyToManyField(to='a_zoom_world.Photo', verbose_name='photo_property', related_name='property_photos')),
                ('property_allergens', models.ManyToManyField(to='a_zoom_world.PotentialAllergen')),
                ('property_amenity', models.ManyToManyField(to='a_zoom_world.Amenity')),
                ('type_id', models.ForeignKey(to='a_zoom_world.DomicileType')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyNeed',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('accessibility_need', models.ForeignKey(to='a_zoom_world.AccessibilityNeed')),
                ('property_id', models.ForeignKey(to='a_zoom_world.Property')),
                ('property_need', models.ManyToManyField(to='a_zoom_world.NeedException')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('make', models.CharField(max_length=50, default=None)),
                ('model', models.CharField(max_length=50, default=None)),
                ('description', models.CharField(max_length=500, default=None)),
                ('access_needs', models.ManyToManyField(to='a_zoom_world.AccessibilityNeed')),
                ('property_id', models.ForeignKey(to='a_zoom_world.Property')),
            ],
        ),
        migrations.CreateModel(
            name='ZoomUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('accessibility_need', models.ForeignKey(to='a_zoom_world.AccessibilityNeed')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(load_potential_allergen, reverse_func),
        migrations.RunPython(load_service_amenties, reverse_func),
        migrations.RunPython(load_domicile_type, reverse_func),
        migrations.RunPython(load_accessibility_needs, reverse_func),

    ]
