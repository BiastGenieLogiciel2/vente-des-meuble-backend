from django.db import models

# Create your models here.
class create(models.Model):
    nom = models.CharField(max_length=150)
    email = models.EmailField()
    password = models.CharField(max_length=200)