from django.db import models



# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    name = models.CharField(max_length=30)
    admno = models.CharField(max_length=30, blank=True, unique=True)
    grade = models.CharField(max_length=30)    
    GENDER_CHOICES = (
    ('0', 'Male'),
    ('1', 'Female'),
    )
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    age = models.PositiveSmallIntegerField()
    subjects = models.ManyToManyField(Subject, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.admno:
            last_student = Student.objects.order_by('-id').first()
            if last_student and last_student.admno.isdigit():
                self.admno = str(int(last_student.admno) + 1)
            else:
                self.admno = '257'
        super().save(*args, **kwargs)

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
    grade_assigned = models.CharField(max_length=30, default='-')
    subjects = models.ManyToManyField(Subject, blank=True)

    def __str__(self):
        return self.name
