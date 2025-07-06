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

    def __str__(self):
        return self.name