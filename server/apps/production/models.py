from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.
class AircraftModel(models.Model):
    name = models.SlugField(max_length=50, primary_key=True, blank=False)
    desc = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return self.name

class AircraftPart(models.Model):
    name = models.SlugField(max_length=50, primary_key=True, blank=False)
    desc = models.CharField(max_length=300, blank=True, default='')

    def __str__(self):
        return self.name
    

