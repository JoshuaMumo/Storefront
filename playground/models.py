from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    admno = models.CharField(max_length=30)
    grade = models.CharField(max_length=30)    
    GENDER_CHOICES = (
    ('0', 'Male'),
    ('1', 'Female'),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    age = models.PositiveSmallIntegerField()
    subjects = models.ManyToManyField(Subject, blank=True)



    def __str__(self):
        return self.name
    class Meta:
        ordering = ['grade']
        verbose_name_plural = 'Students'

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    GENDER_CHOICES = (
    ('0', 'Male'),
    ('1', 'Female'),
    )    
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    age = models.PositiveSmallIntegerField()
    grade_assigned = models.CharField(max_length=30, default='Unassigned')
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name
