from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from apps.coordinators.models.coordinator import Coordinator

User = get_user_model()

@receiver(post_save, sender=User)
def create_coordinator_profile(sender, instance, created, **kwargs):
    if created and instance.groups.filter(name="Coordinador").exists():
        # Solo crea perfil si aún no existe y pertenece al grupo Coordinador
        Coordinator.objects.get_or_create(user=instance)
