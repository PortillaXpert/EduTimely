from datetime import timedelta, datetime

from django.core.exceptions import ValidationError
from django.db import models

from apps.environments.models.environment import Environment
from apps.periods.models import Period
from apps.program.models import Program, Skill
from apps.teachers.models.teacher import Teacher


class Schedule(models.Model):
    class CourseDuration(models.IntegerChoices):
        ONEHOUR = 1, '1 Hour'
        TWOHOUR = 2, '2 Hour'

    period = models.ForeignKey(Period, on_delete=models.CASCADE)
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)
    start_time = models.TimeField()

    courseDuration = models.IntegerField(
        choices=CourseDuration.choices,
        default=CourseDuration.ONEHOUR)

    end_time = models.TimeField(blank=True,
                                null=True)

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = "Schedules"
        unique_together = ('environment','teacher', 'program')

    def clean(self):
        super().clean()

        if self.courseDuration < 1:
            raise ValidationError("Course duration must be greater than 0.")

        if self.start_time is not None:
            duration = timedelta(hours=self.courseDuration)
            dt_start = datetime.combine(datetime.today(), self.start_time)
            dt_end = dt_start + duration
            new_start = self.start_time
            new_end = dt_end.time()

            overlapping = Schedule.objects.filter(
                environment=self.environment,
                day=self.day
            ).exclude(id=self.id).filter(
                start_time__lt=new_end,
                end_time__gt=new_start,
            )

            if overlapping.exists():
                raise ValidationError("This schedule overlaps with another in the same environment.")


    def save(self, *args, **kwargs):
        if self.start_time is not None and self.courseDuration is not None:
            duration = timedelta(hours=self.courseDuration)
            dt_start = datetime.combine(datetime.today(), self.start_time)
            self.end_time = (dt_start + duration).time()
        self.full_clean()
        super().save(*args, **kwargs)
