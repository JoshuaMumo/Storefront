from django import forms
from .models import Student, Teacher

class StudentSignUpForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ('admno',)
        
class StudentSignInForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'admno')
        
class TeacherSignUpForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ('id','grade_assigned')
        
class TeacherSignInForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'id')
        
