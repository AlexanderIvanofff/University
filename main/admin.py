from django.contrib import admin
from .models import Student, Course


class CourseLine(admin.TabularInline):
    model = Student


class StudentAdmin(admin.ModelAdmin):
    inlines = [
        CourseLine,
    ]


admin.site.register(Course)
admin.site.register(Student)
