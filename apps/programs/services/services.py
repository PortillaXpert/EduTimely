from apps.programs.models.programs import Programs
from django.core.exceptions import ValidationError
from django.db import transaction


class Services:

    @staticmethod
    def list_programs():
        return Programs.objects.all()

    @staticmethod
    def create_program(name):
        if Programs.objects.filter(name__iexact=name).exists():
            raise ValidationError("Ya existe un programa con este nombre.")
        return Programs.objects.create(name=name)

    @staticmethod
    def update_program(program_id, name):
        if Programs.objects.exclude(id=program_id).filter(name__iexact=name).exists():
            raise ValidationError("Ya existe un programa con este nombre.")
        program = Programs.objects.get(id=program_id)
        program.name = name
        program.save()
        return program

    @staticmethod
    def delete_program(program_id):
        Programs.objects.get(id=program_id).delete()
