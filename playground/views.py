from multiprocessing import AuthenticationError
import subprocess
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
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

def update_teacher(request):
    return render(request, 'update_teacher.html')

def update_teacher_profile(request, teacher_name):
    teacher = get_object_or_404(Teacher, name=teacher_name)
    if request.method == 'POST':
        teacher.grade_assigned = request.POST.get('grade_assigned')
        teacher.save()
        return redirect('teachers')
    return render(request, 'update_teacher.html', {'teacher': teacher})

def delete_teacher(request, teacher_name):
    teacher = get_object_or_404(Teacher, name=teacher_name)
    teacher.delete()
    return redirect('teachers')

def delete_student(request, student_name):
    student = get_object_or_404(Student, name=student_name)
    student.delete()
    return redirect('student')

def delete_subject(request, subject_name):
    subject = get_object_or_404(Subject, name=subject_name)
    subject.delete()
    return redirect('subjects')