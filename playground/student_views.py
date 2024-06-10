from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import StudentSignUpForm


def student_signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))  # Redirect to home page after successful login
        else:
            return render(request, 'student_signin.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'student_signin.html')

def student(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students')
    else:
        form = StudentSignUpForm()
    return render(request, 'student.html', {'form': form})