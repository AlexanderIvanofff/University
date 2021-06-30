from django.contrib import admin
from django.urls import path
from main.views import list_student, course_list, list_professor, list_title

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_student),
    path('courses/', course_list),
    path('professor/', list_professor),
    path('titles/', list_title)

]
