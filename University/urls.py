from django.contrib import admin
from django.urls import path
from main.views import CourseView, ProfessorView, TitleView, StudentView, StudentsAndCoursesCredits, \
    TeacherDisciplinesAndStudentsCount, TopCourses, TopProfessors, DeleteStudent

urlpatterns = [
    path('admin/', admin.site.urls),
    path('total_students/', StudentView.as_view()),
    path('total_students/<int:student_id>/delete/', DeleteStudent.delete_students),
    path('courses/', CourseView.as_view()),
    path('professor/', ProfessorView.as_view()),
    path('titles/', TitleView.as_view()),
    path('students-courses-credits/', StudentsAndCoursesCredits.as_view()),
    path('professor-courses-student-count/', TeacherDisciplinesAndStudentsCount.as_view()),
    path('top-courses/', TopCourses.as_view()),
    path('top-professors/', TopProfessors.as_view()),
]
