from django.db import models
from apps.users.models.user import CustomUser
from apps.environments.models.environment import Environment
from apps.programs.models.programs import Programs
from apps.periods.models.period import Period


class Schedule(models.Model):
    DAY_CHOICES = [
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIÉRCOLES', 'Miércoles'),
        ('JUEVES', 'Jueves'),
        ('VIERNES', 'Viernes'),
    ]

    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='schedules')
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='schedules')
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE, related_name='schedules')
    program = models.ForeignKey(Programs, on_delete=models.CASCADE, related_name='schedules')

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'
        ordering = ['day', 'start_time']
        unique_together = ('period', 'teacher', 'day', 'start_time', 'environment')

    def __str__(self):
        return f"{self.teacher.get_full_name()} - {self.day} {self.start_time}-{self.end_time}"
