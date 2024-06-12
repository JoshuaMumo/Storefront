from multiprocessing import AuthenticationError
import subprocess
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
import psutil
from .models import Student, Subject, Teacher
from Demos.win32ts_logoff_disconnected import username
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from aiohttp.client import request



def home(request):
    return render(request, 'home.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
            
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
    context = {}
    return render(request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('logout')
def about(request):
    return render(request, 'about.html')

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

def subjects_view(request):
    subjects = Subject.objects.all()
    return render(request, 'subjects.html', {'subjects': subjects})

def add_teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        teacher = Teacher(name=name, email=email)
        teacher.save()
        return redirect('teachers')
    return render(request, 'add_teacher.html')

def update_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    if request.method == 'POST':
        teacher.name = request.POST.get('name')
        teacher.save()
        return redirect('teachers')
    return render(request, 'update_teacher.html', {'teacher': teacher})