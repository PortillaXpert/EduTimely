from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

class Period(models.Model):
    class PeriodLength(models.IntegerChoices):
        THREE_MONTHS = 3, '3 Months'
        SIX_MONTHS = 6, '6 Months'
        TWELVE_MONTHS = 12, '12 Months'

    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    period_length = models.PositiveIntegerField(choices=PeriodLength.choices, default=PeriodLength.THREE_MONTHS)
    is_active = models.BooleanField(default=True)

    def validate_period_overlap(self):
        if self.end_date:
            overlap = Period.objects.filter(
                ~Q(pk=self.pk),
                Q(start_date__lte=self.end_date),
                Q(end_date__gte=self.start_date)
            ).exists()

            if overlap:
                raise ValidationError("Period overlaps with existing periods.")

    def clean(self):
        super().clean()

        if self.end_date and self.start_date > self.end_date:
            raise ValidationError("Start date must be before end date.")

        self.validate_period_overlap()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
