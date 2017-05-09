from __future__ import unicode_literals

from django.db import models

class URL(models.Model):
    url = models.CharField(max_length=1000)