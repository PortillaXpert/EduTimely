from django.db import models
from django.core.exceptions import ValidationError

class Period(models.Model):
    DURATION_CHOICES = [(3, '3 Meses'), (6, '6 Meses')]

    name = models.CharField(max_length=50, unique=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(choices=DURATION_CHOICES, default=3)
    is_active = models.BooleanField(default=True)

    def clean(self):
        super().clean()
        if self.end_date and self.start_date > self.end_date:
            raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        self.validate_overlapping_periods()

    def validate_overlapping_periods(self):
        if not self.end_date:
            return
        existing_periods = Period.objects.exclude(pk=self.pk)
        for period in existing_periods:
            if (
                self.start_date <= period.end_date and self.end_date >= period.start_date
            ):
                raise ValidationError("Existe un período académico que se superpone con las fechas dadas.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
