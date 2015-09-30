# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accessibilityneed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNeeds',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('accessibility_need', models.ForeignKey(to='accessibilityneed.AccessibilityNeed')),
            ],
        ),
        migrations.CreateModel(
            name='ZoomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='userneeds',
            name='user_id',
            field=models.ForeignKey(to='user.ZoomUser'),
        ),
    ]
