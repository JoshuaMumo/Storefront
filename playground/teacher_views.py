from django.shortcuts import render, redirect
from playground.models import Teacher
from .forms import TeacherSignUpForm, TeacherSignInForm
from django.contrib.auth.models import User


def teacher_signin(request):
    if request.method == 'POST':
        form = TeacherSignInForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teachers/')  
    else:
        form = TeacherSignInForm()
    return render(request, 'teacher_signin.html', {'form': form})

def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            # Create the teacher instance
            teacher = Teacher(
                user=User,
                name=form.cleaned_data['name'],
                gender=form.cleaned_data['gender'],
                age=form.cleaned_data['age'],
            )
            teacher.save()

            # Save many-to-many relationships (subjects)
            teacher.subjects.set(form.cleaned_data['subjects'])

            return redirect('/teacher_signin/')  # Redirect to the teacher sign-in page
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher_signup.html', {'form': form})