from django.db import models

class SkillProgram(models.Model):
    program = models.ForeignKey('Program', on_delete=models.CASCADE)
    skill = models.ForeignKey('Skill', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('program', 'skill')