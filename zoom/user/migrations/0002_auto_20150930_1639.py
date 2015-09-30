# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accessibilityneed', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userneeds',
            name='accessibility_need',
        ),
        migrations.RemoveField(
            model_name='userneeds',
            name='user_id',
        ),
        migrations.AddField(
            model_name='zoomuser',
            name='accessibility_need',
            field=models.ForeignKey(default=1, to='accessibilityneed.AccessibilityNeed'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zoomuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserNeeds',
        ),
    ]
