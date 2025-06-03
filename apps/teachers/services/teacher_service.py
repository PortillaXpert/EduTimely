from apps.teachers.models.teacher import Teacher
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class TeacherService:

    @staticmethod
    def get_by_user(user):
        return Teacher.objects.filter(user=user).first()

    @staticmethod
    def get_by_id(teacher_id):
        return Teacher.objects.select_related("user").filter(id=teacher_id).first()

    @staticmethod
    def list_all():
        return Teacher.objects.select_related("user").all()

    @staticmethod
    def create_teacher(user: User, document_number: str, phone: str = '', address: str = ''):
        if Teacher.objects.filter(user=user).exists():
            raise ValidationError("Este usuario ya tiene un perfil de docente.")
        if Teacher.objects.filter(document_number=document_number).exists():
            raise ValidationError("Ya existe un docente con este número de documento.")
        return Teacher.objects.create(
            user=user,
            document_number=document_number,
            phone=phone,
            address=address
        )

    @staticmethod
    def update_teacher(teacher: Teacher, data: dict):
        user = teacher.user

        if Teacher.objects.exclude(id=teacher.id).filter(document_number=data['document_number']).exists():
            raise ValidationError("Ya existe un docente con este número de documento.")

        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.save()

        teacher.document_number = data.get('document_number', teacher.document_number)
        teacher.phone = data.get('phone', teacher.phone)
        teacher.address = data.get('address', teacher.address)
        teacher.save()

        return teacher

    @staticmethod
    def delete_teacher(teacher_id):
        Teacher.objects.filter(id=teacher_id).delete()
