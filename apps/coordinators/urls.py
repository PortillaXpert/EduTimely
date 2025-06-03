from django.urls import path
from apps.coordinators.views.coordinator_views import coordinator_detail, coordinator_update

app_name = "coordinators"

urlpatterns = [
    path("", coordinator_detail.as_view(), name="detail"),
    path("editar/", coordinator_update.as_view(), name="edit"),
]
