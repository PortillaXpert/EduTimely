from apps.coordinators.models.coordinator import Coordinator
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class CoordinatorService:

    @staticmethod
    def get_by_user(user):
        return Coordinator.objects.filter(user=user).first()

    @staticmethod
    def list_all():
        return Coordinator.objects.select_related('user').all()

    @staticmethod
    def update_coordinator(coordinator: Coordinator, data: dict):
        """
        Actualiza tanto el modelo Coordinator como los datos del usuario relacionado.
        Espera que data contenga claves: first_name, last_name, email, document_number, phone, address.
        """
        user = coordinator.user

        # Validación de duplicidad de documento
        if Coordinator.objects.exclude(id=coordinator.document_number).filter(document_number=data['document_number']).exists():
            raise ValidationError("Ya existe un coordinador con este número de documento.")

        # Actualizar datos del usuario
        user.first_name = data.get('first_name', user.first_name)
        user.last_name = data.get('last_name', user.last_name)
        user.email = data.get('email', user.email)
        user.save()

        # Actualizar datos del coordinador
        coordinator.document_number = data.get('document_number', coordinator.document_number)
        coordinator.phone = data.get('phone', coordinator.phone)
        coordinator.address = data.get('address', coordinator.address)
        coordinator.save()

        return coordinator

    @staticmethod
    def create_coordinator(user: User, document_number: str, phone: str = '', address: str = ''):
        if Coordinator.objects.filter(user=user).exists():
            raise ValidationError("Este usuario ya tiene un perfil de coordinador.")
        if Coordinator.objects.filter(document_number=document_number).exists():
            raise ValidationError("Ya existe un coordinador con este número de documento.")
        return Coordinator.objects.create(
            user=user,
            document_number=document_number,
            phone=phone,
            address=address
        )

    @staticmethod
    def delete_coordinator(coordinator_id):
        Coordinator.objects.filter(id=coordinator_id).delete()
