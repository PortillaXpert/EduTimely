from django.urls import path
from apps.periods.views.period_views import period_create, period_list

app_name = 'periods'

urlpatterns = [
    path('', period_list, name='list'),
    path('nuevo/', period_create, name='create'),
]
