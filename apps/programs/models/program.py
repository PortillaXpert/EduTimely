from django.db import models

from apps.programs.models.skill import Skill


class Program(models.Model):
    name = models.CharField(max_length=100)
    competencias = models.ManyToManyField(Skill, through='SkillProgram')

    def __str__(self):
        return self.name