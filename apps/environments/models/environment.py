from django.core.exceptions import ValidationError
from django.db import models

class Environment(models.Model):
    class Env_types(models.TextChoices):
        IN_PERSON = 'IN_PERSON', 'In-Person'
        VIRTUAL = 'VIRTUAL', 'Virtual'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    env_type = models.CharField(
        max_length=15,
        choices= Env_types.choices,
        default=Env_types.VIRTUAL)
    capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def validate_capacity(self):
        if self.capacity < 1:
            raise ValidationError('Capacity must be greater than 0')
        elif self.capacity > 100:
            raise ValidationError('Capacity must be less than 100')

    def clean(self):
        super().clean()
        if self.env_type == self.Env_types.VIRTUAL and self.location.strip().lower() != 'online':
            raise ValidationError({'location': 'Virtual environments must have location "Online"'})
        self.validate_capacity()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name