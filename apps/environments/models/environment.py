from django.db import models
from django.utils.translation import gettext_lazy as _


class Environment(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Nombre del Ambiente"))

    class Meta:
        verbose_name = _("Ambiente")
        verbose_name_plural = _("Ambientes")
        ordering = ['name']

    def __str__(self):
        return self.name
