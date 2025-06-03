from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    document_number = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.document_number}"

    def clean(self):
        # Validación para asegurar que el usuario no sea coordinador y docente al mismo tiempo
        if self.user.groups.filter(name="Coordinador").exists():
            raise ValidationError("Este usuario ya está registrado como Coordinador.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Llama a `clean()` para validar antes de guardar
        super().save(*args, **kwargs)
