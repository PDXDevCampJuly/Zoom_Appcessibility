from django.db import models
from accessibilityneed.models import AccessibilityNeed

# Create your models here.


class ZoomUser(models.Model):
    """ This table holds the user information using django default"""





class UserNeeds(models.Model):
    """ This table holds the users needs information"""

    user_id = models.ForeignKey(ZoomUser)
    accessibility_need = models.ForeignKey(AccessibilityNeed)

