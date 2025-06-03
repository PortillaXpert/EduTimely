from django.urls import path
from apps.coordinators.views import coordinator_views

app_name = "coordinators"

urlpatterns = [
    path("", coordinator_views.coordinator_detail, name="detail"),
    path("editar/", coordinator_views.coordinator_update, name="edit"),
]
