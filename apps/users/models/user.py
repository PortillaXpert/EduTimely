from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):


    @property
    def is_coordinator(self):
        return self.groups.filter(name="Coordinador").exists()

    @property
    def is_teacher(self):
        return self.groups.filter(name="Docente").exists()