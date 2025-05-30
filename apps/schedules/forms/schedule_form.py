from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from apps.schedules.models.schedule import Schedule
from apps.schedules.services.schedule_service import ScheduleService


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['period', 'instructor', 'program', 'environment', 'day', 'start_time', 'end_time']
        widgets = {
            'day': forms.Select(attrs={'class': 'form-select'}),
            'start_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'end_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        period = cleaned_data.get('period')
        instructor = cleaned_data.get('instructor')
        program = cleaned_data.get('program')
        environment = cleaned_data.get('environment')
        day = cleaned_data.get('day')
        start_time = cleaned_data.get('start_time')
        end_time = cleaned_data.get('end_time')

        if start_time and end_time and start_time >= end_time:
            raise ValidationError(_("La hora de inicio debe ser anterior a la hora de finalización."))

        if period and instructor and environment and day and start_time and end_time:
            try:

                exclude_id = self.instance.id if self.instance and self.instance.pk else None
                ScheduleService.validate_conflicts(
                    period, environment, instructor, day, start_time, end_time, exclude_id=exclude_id
                )
            except ValidationError as e:
                raise ValidationError(e.messages)

        return cleaned_data
