
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from apps.teachers.models.teacher import Teacher
from apps.teachers.forms.teacher_form import TeacherForm
from apps.shared.decorators.role_required import role_required


@role_required(['DOCENTE'])
def teacher_detail(request):
    """
    Devuelve los datos del docente autenticado en formato JSON.
    """
    teacher = get_object_or_404(Teacher, user=request.user)
    data = {
        "id": teacher.id,
        "document_number": teacher.document_number,
        "phone": teacher.phone,
        "address": teacher.address,
        "first_name": teacher.user.first_name,
        "last_name": teacher.user.last_name,
        "email": teacher.user.email,
    }
    return JsonResponse(data)


@role_required(['DOCENTE'])
def teacher_update(request):
    """
    Permite actualizar los datos del docente autenticado (datos personales y de usuario).
    Recibe POST con campos del formulario.
    """
    teacher = get_object_or_404(Teacher, user=request.user)

    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher, user=request.user)
        if form.is_valid():
            updated = form.save()
            return JsonResponse({"message": "Datos actualizados correctamente."})
        else:
            return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "Método no permitido."}, status=405)
