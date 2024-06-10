import subprocess
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
import psutil
from .forms import StudentSignUpForm, TeacherSignUpForm
from .models import Student, Teacher


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def student_signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and hasattr(user, 'student'):
                login(request, user)
                return redirect('/students/')  # Redirect to the student page
        return render(request, 'student_signin.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'student_signin.html', {'form': form})

def student_signup(request):
    if request.method == 'POST':
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            Student = form.save()
            Student.user = request.user
            Student.save()
            return redirect('/student_signin/')  # Redirect to the student sign-in page
    else:
        form = StudentSignUpForm()
    return render(request, 'student_signup.html', {'form': form})

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

def signout(request):
    return render(request, 'signout.html')

def start_streamlit():
    # Check if Streamlit is already running
    for proc in psutil.process_iter():
        if "streamlit" in proc.name():
            return
    # Start Streamlit subprocess
    subprocess.Popen(["streamlit", "run", "ragchatbot.py"])

def rag_chatbot(request):
    start_streamlit()
    return redirect("http://localhost:8501")

def teachers_view(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher.html', {'teachers': teachers})

def students_view(request):
    students = Student.objects.all()
    return render(request, 'student.html', {'students': students})

def logout_view(request):
    logout(request)