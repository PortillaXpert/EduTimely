from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.schedules.forms.schedule_form import ScheduleForm
from apps.schedules.services.schedule_service import ScheduleService
from apps.shared.decorators.role_required import role_required


@role_required(['COORDINATOR'])
def schedule_list(request):
    schedules = ScheduleService.list_schedules()
    return render(request, 'schedules/schedule_list.html', {'schedules': schedules})


@role_required(['COORDINATOR'])
def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            ScheduleService.create_schedule(
                period=form.cleaned_data['period'],
                instructor=form.cleaned_data['instructor'],
                program=form.cleaned_data['program'],
                environment=form.cleaned_data['environment'],
                day=form.cleaned_data['day'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time']
            )
            messages.success(request, 'Horario creado correctamente.')
            return redirect('schedules:list')
    else:
        form = ScheduleForm()
    return render(request, 'schedules/schedule_form.html', {'form': form})


@role_required(['COORDINATOR'])
def schedule_update(request, schedule_id):
    schedule = get_object_or_404(ScheduleService.list_schedules(), id=schedule_id)

    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            ScheduleService.update_schedule(
                schedule_id=schedule.id,
                period=form.cleaned_data['period'],
                instructor=form.cleaned_data['instructor'],
                program=form.cleaned_data['program'],
                environment=form.cleaned_data['environment'],
                day=form.cleaned_data['day'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time']
            )
            messages.success(request, 'Horario actualizado correctamente.')
            return redirect('schedules:list')
    else:
        form = ScheduleForm(instance=schedule)

    return render(request, 'schedules/schedule_form.html', {'form': form})


@role_required(['COORDINATOR'])
def schedule_delete(request, schedule_id):
    schedule = get_object_or_404(ScheduleService.list_schedules(), id=schedule_id)

    if request.method == 'POST':
        ScheduleService.delete_schedule(schedule_id)
        messages.success(request, 'Horario eliminado correctamente.')
        return redirect('schedules:list')

    return render(request, 'schedules/schedule_confirm_delete.html', {'schedule': schedule})
