from django.db import models

# Create your models here.
class Reto(models.Model):
    phone = models.IntegerField()
    email = models.CharField(max_length=30)