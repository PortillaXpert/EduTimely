from django.urls import path
from apps.schedules.views import schedule_views

app_name = 'schedules'

urlpatterns = [
    path('', schedule_views.schedule_list, name='list'),
    path('create/', schedule_views.schedule_create, name='create'),
    path('update/<int:schedule_id>/', schedule_views.schedule_update, name='update'),
    path('delete/<int:schedule_id>/', schedule_views.schedule_delete, name='delete'),
]
