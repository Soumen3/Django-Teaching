from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=100)
	age = models.IntegerField()
	grade = models.CharField(max_length=10)

	def __str__(self):
		return self.name
	
class Teacher(models.Model):
	name = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)
	phone = models.IntegerField(null=True)

	def __str__(self):
		return self.name