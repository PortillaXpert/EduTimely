from django.urls import path
from apps.teachers.views.teacher_view import teacher_detail, teacher_update

app_name = "teachers"

urlpatterns = [
    path("", teacher_detail, name="detail"),
    path("editar/", teacher_update, name="edit"),
]
