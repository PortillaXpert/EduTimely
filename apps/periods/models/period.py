from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Period(models.Model):
    name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name=_("Nombre del periodo"),
        help_text=_("Ejemplo: '2025-I', '2025-II'")
    )
    start_date = models.DateField(verbose_name=_("Fecha de inicio"))
    end_date = models.DateField(verbose_name=_("Fecha de finalización"))
    is_active = models.BooleanField(default=True, verbose_name=_("¿Está activo?"))

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Creado en"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Actualizado en"))

    class Meta:
        verbose_name = _("Periodo académico")
        verbose_name_plural = _("Periodos académicos")
        ordering = ['-start_date']

    def __str__(self):
        return self.name

    def clean(self):
        # Validar que la fecha de inicio sea anterior a la de fin
        if self.start_date >= self.end_date:
            raise ValidationError(_("La fecha de inicio debe ser anterior a la fecha de finalización."))

        # Validar que no haya solapamiento con otros periodos activos
        overlapping = Period.objects.filter(
            is_active=True,
            end_date__gte=self.start_date,
            start_date__lte=self.end_date
        ).exclude(pk=self.pk)

        if overlapping.exists():
            raise ValidationError(_("Ya existe un periodo activo que se solapa con estas fechas."))

    def save(self, *args, **kwargs):
        self.full_clean()  # Ejecuta clean() antes de guardar
        super().save(*args, **kwargs)
