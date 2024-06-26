from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	grade = models.CharField(max_length=10)
	address = models.TextField(default="None")

	def __str__(self):
		return self.name