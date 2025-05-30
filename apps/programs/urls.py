from django.urls import path
from apps.programs.views import views

app_name = 'programs'

urlpatterns = [
    path('', views.program_list, name='list'),
    path('crear/', views.program_create, name='create'),
    path('editar/<int:program_id>/', views.program_update, name='update'),
    path('eliminar/<int:program_id>/', views.program_delete, name='delete'),
]
