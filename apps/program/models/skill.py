from django.db import models

class Skill(models.Model):
    class SType(models.TextChoices):
        GENERIC = 'gen', 'Generic'
        SPECIFIC = 'spec', 'Specific'

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20,
                            choices=SType.choices,
                            default=SType.GENERIC)

    def __str__(self):
        return self.name
