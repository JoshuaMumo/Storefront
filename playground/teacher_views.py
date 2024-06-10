from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import TeacherSignUpForm
from .models import Teacher

def teacher_signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and hasattr(user, 'teacher'):
                login(request, user)
                return redirect('/teachers/')  # Redirect to the teacher page
        return render(request, 'teacher_signin.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'teacher_signin.html', {'form': form})

def teacher_signup(request):
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            teacher = form.save()
            teacher.user = request.user
            teacher.save()
            return redirect('/teacher_signin/')  # Redirect to the teacher sign-in page
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher_signup.html', {'form': form})