from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.programs.forms.program_form import Program_Form
from apps.programs.services.services import Services
from apps.shared.decorators.role_required import role_required


@role_required(['COORDINATOR'])
def program_list(request):
    programs = Services.list_programs()
    return render(request, 'programs/program_list.html', {'programs': programs})


@role_required(['COORDINATOR'])
def program_create(request):
    if request.method == 'POST':
        form = Program_Form(request.POST)
        if form.is_valid():
            try:
                Services.create_program(name=form.cleaned_data['name'])
                messages.success(request, 'Programa creado exitosamente.')
                return redirect('programs:list')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = Program_Form()
    return render(request, 'programs/program_form.html', {'form': form})


@role_required(['COORDINATOR'])
def program_update(request, program_id):
    program = get_object_or_404(Services.list_programs(), id=program_id)
    if request.method == 'POST':
        form = Program_Form(request.POST, instance=program)
        if form.is_valid():
            try:
                Services.update_program(program_id=program.id, name=form.cleaned_data['name'])
                messages.success(request, 'Programa actualizado exitosamente.')
                return redirect('programs:list')
            except Exception as e:
                form.add_error(None, str(e))
    else:
        form = Program_Form(instance=program)
    return render(request, 'programs/program_form.html', {'form': form})


@role_required(['COORDINATOR'])
def program_delete(request, program_id):
    program = get_object_or_404(Services.list_programs(), id=program_id)
    if request.method == 'POST':
        Services.delete_program(program_id)
        messages.success(request, 'Programa eliminado correctamente.')
        return redirect('programs:list')
    return render(request, 'programs/program_confirm_delete.html', {'program': program})
