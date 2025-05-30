from apps.environments.models.environment import Environment
from django.core.exceptions import ValidationError


class EnvironmentService:

    @staticmethod
    def list_environments():
        return Environment.objects.all()

    @staticmethod
    def create_environment(name):
        if Environment.objects.filter(name__iexact=name).exists():
            raise ValidationError("Ya existe un ambiente con este nombre.")
        return Environment.objects.create(name=name)

    @staticmethod
    def update_environment(environment_id, name):
        if Environment.objects.exclude(id=environment_id).filter(name__iexact=name).exists():
            raise ValidationError("Ya existe un ambiente con este nombre.")
        environment = Environment.objects.get(id=environment_id)
        environment.name = name
        environment.save()
        return environment

    @staticmethod
    def delete_environment(environment_id):
        Environment.objects.get(id=environment_id).delete()
