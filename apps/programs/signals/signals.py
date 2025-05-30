from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from apps.programs.models.programs import Programs
import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Programs)
def log_program_saved(sender, instance, created, **kwargs):
    if created:
        logger.info(f"Programa creado: {instance.name}")
    else:
        logger.info(f"Programa actualizado: {instance.name}")

@receiver(post_delete, sender=Programs)
def log_program_deleted(sender, instance, **kwargs):
    logger.info(f"Programa eliminado: {instance.name}")
