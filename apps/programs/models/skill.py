from django.db import models


class Skill(models.Model):
    TYPE_SKILL = [
        ('generic', 'Generic'),
        ('specific', 'Specific'),
    ]
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE_SKILL)

    def __str__(self):
        return self.name