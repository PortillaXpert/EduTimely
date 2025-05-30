from django.db import models
from django.utils.translation import gettext_lazy as _


class Programs(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Nombre del Programa"))

    class Meta:
        verbose_name = _("Programa")
        verbose_name_plural = _("Programas")
        ordering = ['name']

    def __str__(self):
        return self.name
