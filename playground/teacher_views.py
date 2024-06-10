from django.shortcuts import render, redirect
from .forms import TeacherSignUpForm, TeacherSignInForm



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
            form.save()
            return redirect('/teachers')
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher_signup.html', {'form': form})