from django.db import models
from .choices import GENDER_CHOICES


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    admno = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    age = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

