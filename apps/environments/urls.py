from django.urls import path
from apps.environments.views import environment_views as views

app_name = 'environments'

urlpatterns = [
    path('', views.environment_list, name='list'),
    path('crear/', views.environment_create, name='create'),
    path('<int:environment_id>/editar/', views.environment_update, name='update'),
    path('<int:environment_id>/eliminar/', views.environment_delete, name='delete'),
]
