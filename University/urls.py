from django.contrib import admin
from django.urls import path
from main.views import CourseView, ProfessorView, TitleView, StudentView, StudentsAndCoursesCredits, \
    TeacherDisciplinesAndStudentsCount, TopCourses

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StudentView.as_view()),
    path('courses/', CourseView.as_view()),
    path('professor/', ProfessorView.as_view()),
    path('titles/', TitleView.as_view()),
    path('students-courses-credits/', StudentsAndCoursesCredits.as_view()),
    path('professor-courses-student-count/', TeacherDisciplinesAndStudentsCount.as_view()),
    path('top-courses/', TopCourses.as_view()),
]
