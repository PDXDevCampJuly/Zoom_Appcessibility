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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=200)),
                ('description', models.CharField(default=None, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('street', models.CharField(default=None, max_length=200)),
                ('street_two', models.CharField(default=None, max_length=200)),
                ('city', models.CharField(default=None, max_length=50)),
                ('state', models.CharField(default=None, max_length=50)),
                ('zip_code', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('type', models.CharField(default=None, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DomicileType',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NeedException',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('need', models.CharField(default=None, max_length=200)),
                ('room_location', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PotentialAllergen',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description', models.CharField(default=None, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('accessibility_need', models.ForeignKey(to='a_zoom_world.AccessibilityNeed')),
                ('property_id', models.ForeignKey(to='a_zoom_world.Property')),
                ('property_need', models.ManyToManyField(to='a_zoom_world.NeedException')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('accessibility_need', models.ForeignKey(to='a_zoom_world.AccessibilityNeed')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
