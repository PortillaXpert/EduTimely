# apps/periods/signals.py

from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.periods.models.period import Period

@receiver(pre_save, sender=Period)
def ensure_only_one_active_period(sender, instance, **kwargs):
    """
    Asegura que solo exista un periodo activo a la vez.
    Si el periodo que se va a guardar está activo, desactiva los demás.
    """
    if instance.is_active:
        sender.objects.exclude(pk=instance.pk).filter(is_active=True).update(is_active=False)
