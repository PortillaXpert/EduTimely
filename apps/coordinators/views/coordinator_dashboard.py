from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.shared.decorators.role_required import role_required
from apps.schedules.models.schedule import Schedule
from apps.environments.models.environment import Environment
from apps.programs.models.programs import Programs
from apps.users.models import CustomUser
from apps.periods.models import Period
from django.utils.decorators import method_decorator


@method_decorator(role_required(['COORDINATOR']), name='dispatch')
class CoordinatorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "coordinators/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_docentes"] = CustomUser.objects.filter(role='TEACHER').count()
        context["total_programas"] = Programs.objects.count()
        context["total_ambientes"] = Environment.objects.count()
        context["total_horarios"] = Schedule.objects.count()
        context["periodo_actual"] = Period.objects.filter(is_active=True).first()
        return context
