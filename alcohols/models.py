from django.db import models

# Create your models here.
class Alcohol(models.Model):
    product = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    degree = models.CharField(max_length=10)
    ingredient = models.CharField(max_length=200)
    volume = models.CharField(max_length=10)