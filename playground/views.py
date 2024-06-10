import subprocess
from django.shortcuts import render, redirect
import psutil
from .models import Student, Teacher


def home(request):
    return render(request, 'home.html')

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
