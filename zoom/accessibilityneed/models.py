from django.db import models
# Create your models here.


class AccessibilityNeed(models.Model):
    """ This table holds the list of accessibility needs"""

    name = models.CharField(max_length=200, default=None)
    description = models.CharField(max_length=1000, default=None)







