from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import StudentForm, CoursesForm, ProfessorForm, TitleForm
from .models import Student, Course, Professors, Title
from .queries import get_students_and_there_courses_credits, get_teacher_disciplines_and_students_count, \
    get_top_courses, get_top_professors


class StudentsAndCoursesCredits(View):
    def get(self, request, *args, **kwargs):
        students = Student.objects.raw(get_students_and_there_courses_credits())

        context = {'students': students}
        return render(request, 'get_students_and_there_courses_credits.html', context)


class TeacherDisciplinesAndStudentsCount(View):
    def get(self, request, *args, **kwargs):
        professors = Professors.objects.raw(get_teacher_disciplines_and_students_count())

        context = {'professors': professors}
        return render(request, 'get_professors_and_there_courses_and_student_count.html', context)


class TopCourses(View):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.raw(get_top_courses())
        context = {'courses': courses}
        return render(request, 'get_top_courses.html', context)


class TopProfessors(View):
    def get(self, request, *args, **kwargs):
        professors = Professors.objects.raw(get_top_professors())
        context = {'professors': professors}
        return render(request, 'get_top_professors.html', context)


class StudentView(View):
    form = StudentForm()

    def get(self, request, *args, **kwargs):
        students = Student.objects.all()
        context = {'students': students, 'form': self.form}
        return render(request, 'students.html', context)

    def post(self, request, *args, **kwargs):
        students = Student.objects.all()

        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = StudentForm()
        context = {'students': students, 'form': form}
        return render(request, 'students.html', context)


class CourseView(View):
    form = CoursesForm()

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        context = {'courses': courses, 'form': self.form}
        return render(request, 'courses.html', context)

    def post(self, request, *args, **kwargs):
        courses = Course.objects.all()
        form = CoursesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = CoursesForm()
        context = {'courses': courses, 'form': form}
        return render(request, 'courses.html', context)


class ProfessorView(View):
    form = ProfessorForm()

    def get(self, request, *args, **kwargs):
        professor = Professors.objects.all()
        context = {'professor': professor, 'form': self.form}
        return render(request, 'professor.html', context)

    def post(self, request, *args, **kwargs):
        professor = Professors.objects.all()
        form = ProfessorForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ProfessorForm()
        context = {'professor': professor, 'form': form}
        return render(request, 'professor.html', context)


class TitleView(View):
    form = TitleForm()

    def get(self, request, *args, **kwargs):
        title = Title.objects.all()
        context = {'title': title, 'form': self.form}
        return render(request, 'title.html', context)

    def post(self, request, *args, **kwargs):
        title = Title.objects.all()
        form = TitleForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = TitleForm()
        context = {'title': title, 'form': form}
        return render(request, 'title.html', context)
