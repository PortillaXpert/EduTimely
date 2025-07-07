from django.db import models

from apps.periods.models.period import Period
from apps.program.models import Program


class PeriodProgram(models.Model):
    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Offered program'
        verbose_name_plural = 'Offered programs'
        unique_together = ('period', 'program')
        ordering = ['period', 'program']

    def __str__(self):
        return f"´{self.program.name} - {self.period.name}"