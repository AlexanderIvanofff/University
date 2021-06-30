from django.forms import ModelForm
from .models import Student, Course, Professors, Title


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'courses']


class CoursesForm(ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'credits', 'professor']


class ProfessorForm(ModelForm):
    class Meta:
        model = Professors
        fields = ['first_name', 'last_name', 'titles']


class TitleForm(ModelForm):
    class Meta:
        model = Title
        fields = ['title_name']