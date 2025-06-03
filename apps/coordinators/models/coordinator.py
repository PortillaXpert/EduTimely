from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Coordinator(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='coordinator_profile',
        verbose_name=_("Usuario")
    )
    document_number = models.CharField(max_length=20, unique=True, verbose_name=_("Número de Documento"))
    phone = models.CharField(max_length=15, verbose_name=_("Teléfono"))
    address = models.CharField(max_length=255, verbose_name=_("Dirección"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de Creación"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Última Actualización"))

    class Meta:
        verbose_name = _("Coordinador")
        verbose_name_plural = _("Coordinadores")
        ordering = ['user__last_name']

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.document_number}"
