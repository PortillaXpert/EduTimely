from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    def is_coordinator(self):
        return self.groups.filter(name='Coordinador').exists()

    def is_teacher(self):
        return self.groups.filter(name='Docente').exists()

    def __str__(self):
        return f"{self.username} ({'Coordinador' if self.is_coordinator() else 'Docente'})"
