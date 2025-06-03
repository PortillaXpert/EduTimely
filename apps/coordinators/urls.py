from django.urls import path
from apps.coordinators.views.coordinator_views import coordinator_detail, coordinator_update
from apps.coordinators.views.coordinator_dashboard import CoordinatorDashboardView
app_name = "coordinators"

urlpatterns = [
    path("", CoordinatorDashboardView.as_view(), name="dashboard"),
    path("", coordinator_detail.as_view(), name="detail"),
    path("editar/", coordinator_update.as_view(), name="edit"),
]
