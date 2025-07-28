from django import forms
from apps.schedules.models.schedule import Schedule


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = [
            'period',
            'environment',
            'teacher',
            'program',
            'skill',
            'day',
            'start_time',
            'courseDuration',
        ]
        widgets = {
            'period': forms.Select(attrs={'class': 'form-control'}),
            'environment': forms.Select(attrs={'class': 'form-control'}),
            'teacher': forms.Select(attrs={'class': 'form-control'}),
            'program': forms.Select(attrs={'class': 'form-control'}),
            'skill': forms.Select(attrs={'class': 'form-control'}),
            'day': forms.Select(attrs={'class': 'form-control'}),
            'start_time': forms.TimeInput(
                attrs={'class': 'form-control', 'type': 'time'}
            ),
            'courseDuration': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'period': 'Academic Period',
            'environment': 'Environment (Classroom or Lab)',
            'teacher': 'Instructor',
            'program': 'Training Program',
            'skill': 'Skill / Competency',
            'day': 'Day of the Week',
            'start_time': 'Start Time',
            'courseDuration': 'Course Duration (Hours)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        self.fields['day'].choices = [
            ('Monday', 'Monday'),
            ('Tuesday', 'Tuesday'),
            ('Wednesday', 'Wednesday'),
            ('Thursday', 'Thursday'),
            ('Friday', 'Friday'),
            ('Saturday', 'Saturday'),
        ]
