from django.db import models
from django.contrib.auth.models import User
from accessibilityneed.models import AccessibilityNeed

# Create your models here.


class ZoomUser(models.Model):
    """ This table holds the user information using django default"""

    user = models.OneToOneField(User)
    accessibility_need = models.ForeignKey(AccessibilityNeed)


