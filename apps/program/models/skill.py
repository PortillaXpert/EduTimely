from django.db import models

class Skill(models.Model):
    class SType(models.TextChoices):
        GENERIC = 'generic', 'Generic'
        SPECIFIC = 'specific', 'Specific'

    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20,
                            choices=SType.choices,
                            default=SType.Generic)

    def __str__(self):
        return self.name
