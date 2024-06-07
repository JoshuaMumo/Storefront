from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class StuentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'admno', 'password']