from django.shortcuts import render

from playground.models import Student, Subject, Teacher

def dashboard(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()

    context = {
        'students': students,
        'teachers': teachers,
        'subjects': subjects,
    }
    print("Students:", students.count())
    print("Teachers:", teachers.count())
    print("Subjects:", subjects.count())
    return render(request, 'index.html', context)
