from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.schedules.models.schedule import Schedule
from django.core.exceptions import ValidationError
from apps.schedules.services.schedule_service import ScheduleService


@receiver(pre_save, sender=Schedule)
def validate_schedule_before_save(sender, instance, **kwargs):
    """
    Evita que se guarde un horario con conflictos desde el admin u otras rutas no controladas.
    """
    if instance.pk:
        # Actualización
        ScheduleService.validate_conflicts(
            period=instance.period,
            environment=instance.environment,
            instructor=instance.instructor,
            day=instance.day,
            start_time=instance.start_time,
            end_time=instance.end_time,
            exclude_id=instance.pk
        )
    else:
        # Creación
        ScheduleService.validate_conflicts(
            period=instance.period,
            environment=instance.environment,
            instructor=instance.instructor,
            day=instance.day,
            start_time=instance.start_time,
            end_time=instance.end_time
        )
