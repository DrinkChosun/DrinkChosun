from django.db import models

# Create your models here.
class Store(models.Model):
    store = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
