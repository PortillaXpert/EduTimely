import datetime

from django import forms
from django.utils import timezone

from apps.periods.models.period import Period


class PeriodForm(forms.ModelForm):
    end_date = forms.DateField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=False
    )

    class Meta:
        model = Period
        fields = ['name', 'start_date', 'end_date', 'period_length', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 2025-2'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control datepicker',
                'type': 'date'
            }),
            'period_length': forms.Select(attrs={
                'class': 'form-control'
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
                'role': 'switch',
                'id': 'flexSwitchCheckDefault'
            }),
        }
        labels = {
            'period_length': 'Period Length',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].widget.template_name = 'widgets/checkbox_input.html'

    def clean_start_date(self):


        start_date = self.cleaned_data.get('start_date')
        if self.instance.pk is None and start_date < timezone.now().date():
            raise forms.ValidationError(
                "The start date cannot be earlier than the current date when creating a new academic period."
            )
        return start_date

    def save(self, commit=True):
        instance = super().save(commit=False)
        if instance.start_date and instance.period_length:
            months = instance.period_length
            new_year = instance.start_date.year
            new_month = instance.start_date.month + months
            new_day = instance.start_date.day

            while new_month > 12:
                new_month -= 12
                new_year += 1


            last_day_of_month = (datetime.date(new_year, new_month % 12 or 12, 1) - datetime.timedelta(days=1)).day
            instance.end_date = datetime.date(new_year, new_month % 12 or 12, min(new_day, last_day_of_month))

        if commit:
            instance.save()
        return instance
