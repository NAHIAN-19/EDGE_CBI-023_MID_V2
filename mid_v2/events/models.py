from django.db import models
from datetime import date
class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True, max_length=500)
    date = models.DateField(default=date.today)
    location = models.CharField(max_length=400, null=False, blank=False)
