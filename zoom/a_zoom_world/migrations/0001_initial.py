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
            name='AccessibilityNeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(default=None, max_length=200)),
                ('description', models.CharField(default=None, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('street', models.CharField(default=None, max_length=200)),
                ('street_two', models.CharField(default=None, max_length=200)),
                ('city', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('type', models.CharField(default=None, max_length=500)),
                ('washer', models.BooleanField(default=False)),
                ('dryer', models.BooleanField(default=False)),
                ('service_dog', models.BooleanField(default=False)),
                ('pets', models.BooleanField(default=False)),
                ('internet', models.BooleanField(default=False)),
                ('parking', models.BooleanField(default=False)),
                ('tv', models.BooleanField(default=False)),
                ('pool', models.BooleanField(default=False)),
                ('hot_tub', models.BooleanField(default=False)),
                ('gym', models.BooleanField(default=False)),
                ('fridge', models.BooleanField(default=False)),
                ('microwave', models.BooleanField(default=False)),
                ('coffee', models.BooleanField(default=False)),
                ('tea', models.BooleanField(default=False)),
                ('restaurant', models.BooleanField(default=False)),
                ('cookware', models.BooleanField(default=False)),
                ('utensils', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DomicileType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(default=None, max_length=200)),
                ('house', models.BooleanField(default=False)),
                ('apartment', models.BooleanField(default=False)),
                ('condo', models.BooleanField(default=False)),
                ('loft', models.BooleanField(default=False)),
                ('square_feet', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NeedException',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('need', models.CharField(default=None, max_length=200)),
                ('room_location', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('photo', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='PotentialAllergen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('description', models.CharField(default=None, max_length=500)),
                ('cedar_trees', models.BooleanField(default=False)),
                ('cats_inside', models.BooleanField(default=False)),
                ('dogs_inside', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(default=None, max_length=50)),
                ('description', models.CharField(default=None, max_length=2000)),
                ('num_bedroom', models.CharField(default=None, max_length=20)),
                ('num_bathroom', models.CharField(default=None, max_length=20)),
                ('address', models.ForeignKey(to='a_zoom_world.Address')),
                ('photo_property', models.ManyToManyField(to='a_zoom_world.Photo')),
                ('property_allergens', models.ManyToManyField(to='a_zoom_world.PotentialAllergen')),
                ('property_amenity', models.ManyToManyField(to='a_zoom_world.Amenity')),
                ('type_id', models.ForeignKey(to='a_zoom_world.DomicileType')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyNeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('roll_in_shower', models.BooleanField(default=False)),
                ('grab_rails_in_bathroom', models.BooleanField(default=False)),
                ('visual_impairment', models.BooleanField(default=False)),
                ('hearing_impairment', models.BooleanField(default=False)),
                ('wheelchair_scooter_access', models.BooleanField(default=False)),
                ('electric_bed', models.BooleanField(default=False)),
                ('shower_chair', models.BooleanField(default=False)),
                ('ceiling_track_hoist', models.BooleanField(default=False)),
                ('mobile_hoist', models.BooleanField(default=False)),
                ('pool_hoist', models.BooleanField(default=False)),
                ('accessibility_need', models.ForeignKey(to='a_zoom_world.AccessibilityNeed')),
                ('property_id', models.ForeignKey(to='a_zoom_world.Property')),
                ('property_need', models.ManyToManyField(to='a_zoom_world.NeedException')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('make', models.CharField(default=None, max_length=50)),
                ('model', models.CharField(default=None, max_length=50)),
                ('description', models.CharField(default=None, max_length=500)),
                ('access_needs', models.ManyToManyField(to='a_zoom_world.AccessibilityNeed')),
                ('property_id', models.ForeignKey(to='a_zoom_world.Property')),
            ],
        ),
        migrations.CreateModel(
            name='ZoomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('accessibility_need', models.ForeignKey(to='a_zoom_world.AccessibilityNeed')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
