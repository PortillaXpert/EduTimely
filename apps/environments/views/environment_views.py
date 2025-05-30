from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.environments.forms.environment_form import EnvironmentForm
from apps.environments.service.environment_service import EnvironmentService
from apps.shared.decorators.role_required import role_required


@role_required(['COORDINATOR'])
def environment_list(request):
    environments = EnvironmentService.list_environments()
    return render(request, 'environments/environment_list.html', {'environments': environments})


@role_required(['COORDINATOR'])
def environment_create(request):
    if request.method == 'POST':
        form = EnvironmentForm(request.POST)
        if form.is_valid():
            try:
                EnvironmentService.create_environment(name=form.cleaned_data['name'], capacity=form.cleaned_data['capacity'])
                messages.success(request, 'Ambiente creado exitosamente.')
                return redirect('environments:list')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = EnvironmentForm()
    return render(request, 'environments/environment_form.html', {'form': form})


@role_required(['COORDINATOR'])
def environment_update(request, environment_id):
    environment = get_object_or_404(EnvironmentService.list_environments(), id=environment_id)
    if request.method == 'POST':
        form = EnvironmentForm(request.POST, instance=environment)
        if form.is_valid():
            try:
                EnvironmentService.update_environment(environment_id, form.cleaned_data['name'], form.cleaned_data['capacity'])
                messages.success(request, 'Ambiente actualizado exitosamente.')
                return redirect('environments:list')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = EnvironmentForm(instance=environment)
    return render(request, 'environments/environment_form.html', {'form': form})


@role_required(['COORDINATOR'])
def environment_delete(request, environment_id):
    environment = get_object_or_404(EnvironmentService.list_environments(), id=environment_id)
    if request.method == 'POST':
        EnvironmentService.delete_environment(environment_id)
        messages.success(request, 'Ambiente eliminado correctamente.')
        return redirect('environments:list')
    return render(request, 'environments/environment_confirm_delete.html', {'environment': environment})
