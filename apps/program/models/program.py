from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=100)
    skills = models.ManyToManyField('program.Skill', through='program.SkillProgram')


    def __str__(self):
        return self.name