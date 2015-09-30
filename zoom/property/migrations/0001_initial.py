# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessibilityneed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('street', models.CharField(max_length=200, default=None)),
                ('street_two', models.CharField(max_length=200, default=None)),
                ('city', models.CharField(max_length=50, default=None)),
                ('state', models.CharField(max_length=50, default=None)),
                ('zip_code', models.CharField(max_length=50, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='DomicileType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Exceptions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('need', models.CharField(max_length=200, default=None)),
                ('room_location', models.CharField(max_length=200, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='PotentialAllergen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.CharField(max_length=500, default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50, default=None)),
                ('description', models.CharField(max_length=2000, default=None)),
                ('num_bedroom', models.CharField(max_length=20, default=None)),
                ('num_bathroom', models.CharField(max_length=20, default=None)),
                ('address', models.ForeignKey(to='property.Address')),
                ('photo_property', models.ManyToManyField(to='property.Photo')),
                ('type_id', models.ForeignKey(to='property.DomicileType')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyNeed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('accessibility_need', models.ForeignKey(to='accessibilityneed.AccessibilityNeed')),
                ('property_id', models.ForeignKey(to='property.Property')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('make', models.CharField(max_length=50, default=None)),
                ('model', models.CharField(max_length=50, default=None)),
                ('description', models.CharField(max_length=500, default=None)),
                ('access_needs', models.ManyToManyField(to='accessibilityneed.AccessibilityNeed')),
                ('property_id', models.ForeignKey(to='property.Property')),
            ],
        ),
        migrations.AddField(
            model_name='potentialallergen',
            name='property_allergens',
            field=models.ManyToManyField(to='property.Property'),
        ),
        migrations.AddField(
            model_name='exceptions',
            name='property_need',
            field=models.ManyToManyField(to='property.PropertyNeed'),
        ),
        migrations.AddField(
            model_name='amenity',
            name='property_amenity',
            field=models.ManyToManyField(to='property.Property'),
        ),
    ]
