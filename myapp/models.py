from django.db import models

# Create your models here.
class Feature(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    icon = models.CharField(max_length=200)