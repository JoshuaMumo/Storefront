import subprocess
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
import psutil
from django.shortcuts import redirect
from .forms import StudentForm
from playground.models import Student, Teacher
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            return redirect('/signin/')  # Redirect to a success page or login page
    else:
        form = StudentForm()
        content = {'form': form}
        return render(request, 'signup.html', content)

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
    return render(request, 'index.html', {'teachers': teachers})

def students_view(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

