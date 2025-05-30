from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.environments.models.environment import Environment
import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Environment)
def log_environment_saved(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Ambiente creado: {instance.name}")
    else:
        logger.info(f"Ambiente actualizado: {instance.name}")


@receiver(post_delete, sender=Environment)
def log_environment_deleted(sender, instance, **kwargs):
    logger.info(f"Ambiente eliminado: {instance.name}")
