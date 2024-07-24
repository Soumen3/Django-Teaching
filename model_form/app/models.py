from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(blank=True)
    email = models.EmailField(help_text="Enter a valid email address")
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name