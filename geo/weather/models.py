from django.db import models

# Create your models here.
class coordinate(models.Model):
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)