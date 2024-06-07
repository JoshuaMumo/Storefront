from django import forms
from django.contrib.auth.models import User
from .models import Student, Teacher

class StudentSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    admno = forms.CharField(max_length=20, required=True, label="Admission Number")

    class Meta:
        model = Student
        fields = ['username', 'password', 'confirm_password', 'admno']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        student = Student(user=user, admno=self.cleaned_data['admno'])
        if commit:
            user.save()
            student.save()
        return student

class TeacherSignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True, label="Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    # Add additional fields if necessary

    class Meta:
        model = Teacher
        fields = ['username', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

    def save(self):
        teacher = Teacher.objects.create(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        teacher.save()
