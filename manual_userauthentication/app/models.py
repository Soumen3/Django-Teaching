from django.db import models

# Create your models here.

class employee(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
