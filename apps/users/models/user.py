from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Agrega más campos si es necesario (ej: telefono, documento)

    @property
    def is_coordinator(self):
        return self.groups.filter(name="Coordinador").exists()

    @property
    def is_teacher(self):
        return self.groups.filter(name="Docente").exists()