from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from apps.periods.forms.period_form import PeriodForm
from apps.periods.services.period_service import PeriodService
from apps.shared.decorators.role_required import role_required


@role_required(['COORDINATOR'])
def period_list(request):
    """
    Muestra la lista de períodos académicos, ordenados por fecha de inicio.
    """
    periods = PeriodService.list_periods()
    active_period = PeriodService.get_active_period()
    return render(request, 'periods/period_list.html', {
        'periods': periods,
        'active_period': active_period
    })


@role_required(['COORDINATOR'])
def period_create(request):
    """
    Crea un nuevo período académico. Solo un período puede estar activo a la vez.
    """
    if request.method == 'POST':
        form = PeriodForm(request.POST)
        if form.is_valid():
            PeriodService.create_period(
                name=form.cleaned_data['name'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                is_active=form.cleaned_data['is_active']
            )
            messages.success(request, 'Período académico creado correctamente.')
            return redirect('periods:list')
    else:
        form = PeriodForm()
    return render(request, 'periods/period_form.html', {'form': form})


@role_required(['COORDINATOR'])
def period_update(request, period_id):
    """
    Edita un período académico existente.
    """
    period = get_object_or_404(PeriodService.list_periods(), id=period_id)

    if request.method == 'POST':
        form = PeriodForm(request.POST, instance=period)
        if form.is_valid():
            PeriodService.update_period(
                period_id=period.id,
                name=form.cleaned_data['name'],
                start_date=form.cleaned_data['start_date'],
                end_date=form.cleaned_data['end_date'],
                is_active=form.cleaned_data['is_active']
            )
            messages.success(request, 'Período académico actualizado correctamente.')
            return redirect('periods:list')
    else:
        form = PeriodForm(instance=period)
    return render(request, 'periods/period_form.html', {'form': form})


@role_required(['COORDINATOR'])
def period_delete(request, period_id):
    """
    Elimina un período académico.
    """
    PeriodService.delete_period(period_id)
    messages.success(request, 'Período académico eliminado correctamente.')
    return redirect('periods:list')
