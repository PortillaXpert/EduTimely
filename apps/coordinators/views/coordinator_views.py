from django.contrib import messages
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, UpdateView

from apps.coordinators.models.coordinator import Coordinator
from apps.coordinators.forms.coordinator_form import CoordinatorForm
from apps.shared.decorators.role_required import role_required


@method_decorator(role_required(['COORDINATOR']), name='dispatch')
class CoordinatorDetailView(DetailView):
    model = Coordinator
    template_name = 'coordinators/coordinator_detail.html'

    def get_object(self):
        return Coordinator.objects.get(user=self.request.user)


@method_decorator(role_required(['COORDINATOR']), name='dispatch')
class CoordinatorUpdateView(UpdateView):
    model = Coordinator
    form_class = CoordinatorForm
    template_name = 'coordinators/coordinator_form.html'

    def get_object(self):
        return Coordinator.objects.get(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pasamos el usuario al formulario
        return kwargs

    def form_valid(self, form):
        messages.success(self.request, "Información actualizada correctamente.")
        return super().form_valid(form)

    def get_success_url(self):
        return redirect('coordinators:detail').url
