from django import forms
from .models import Student, Teacher

class StudentSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")


    class Meta:
        model = Student
        fields = ['username', 'password', 'confirm_password']

    

class TeacherSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    # Add additional fields if necessary

    class Meta:
        model = Teacher
        fields = ['username', 'password', 'confirm_password']
