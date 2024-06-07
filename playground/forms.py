from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'admno', 'password']