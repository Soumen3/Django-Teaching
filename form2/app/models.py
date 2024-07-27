from django.db import models

# Create your models here.

class employee (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(null=True,blank=True)
    password  = models.CharField(max_length=100, default='lbrsibs')