from django.contrib import admin
from .models import Student, Course, Professors


class CourseLine(admin.TabularInline):
    model = Student


class ProfessorLine(admin.TabularInline):
    model = Professors


class StudentAdmin(admin.ModelAdmin):
    inlines = [
        CourseLine,
        ProfessorLine,
    ]


admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Professors)
