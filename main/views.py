from django.shortcuts import render

from .forms import StudentForm, CoursesForm, ProfessorForm, TitleForm
from .models import Student, Course, Professors, Title


def list_student(request):
    students = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StudentForm()
    return render(request, 'students.html', context={
        'students': students,
        'form': form,
    })


def course_list(request):
    courses = Course.objects.all()
    if request.method == 'POST':
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CoursesForm()
    return render(request, 'courses.html', context={
        'courses': courses,
        'form': form
    })


def list_professor(request):
    professor = Professors.objects.all()
    if request.method == 'POST':
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProfessorForm()
    return render(request, 'professor.html', context={
        'professor': professor,
        'form': form,
    })


def list_title(request):
    title = Title.objects.all()
    if request.method == 'POST':
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TitleForm()
    return render(request, 'title.html', context={
        'title': title,
        'form': form,
    })

