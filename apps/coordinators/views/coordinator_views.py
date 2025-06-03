from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.coordinators.models.coordinator import Coordinator
from apps.coordinators.forms.coordinator_form import CoordinatorForm
from apps.shared.decorators.role_required import role_required


@role_required(['COORDINATOR'])
def coordinator_detail(request):
    coordinator = get_object_or_404(Coordinator, user=request.user)
    return render(request, 'coordinators/coordinator_detail.html', {'coordinator': coordinator})


@role_required(['COORDINATOR'])
def coordinator_update(request):
    coordinator = get_object_or_404(Coordinator, user=request.user)

    if request.method == 'POST':
        form = CoordinatorForm(request.POST, instance=coordinator, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Información actualizada correctamente.")
            return redirect('coordinators:detail')
    else:
        form = CoordinatorForm(instance=coordinator, user=request.user)

    return render(request, 'coordinators/coordinator_form.html', {'form': form})
