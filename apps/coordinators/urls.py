from django.urls import path
from apps.coordinators.views.coordinator_views import CoordinatorDetailView, CoordinatorUpdateView
from apps.coordinators.views.coordinator_dashboard import CoordinatorDashboardView
app_name = "coordinators"

urlpatterns = [
    path("", CoordinatorDashboardView.as_view(), name="dashboard"),
    path("", CoordinatorDetailView.as_view(), name="detail"),
    path("editar/", CoordinatorUpdateView.as_view(), name="edit"),
]
