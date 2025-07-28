from django import forms

from apps.environments.models.environment import Environment


class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['id', 'name', 'capacity', 'location', 'env_type', 'is_active']

        labels = {
            'id': 'Environment Code',
            'name': 'Environment Name',
            'capacity': 'Maximum Capacity',
            'location': 'Location (e.g., Building or Floor)',
            'env_type': 'Environment Type',
            'is_active': 'Active Status',
        }

        widgets = {
            'id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., AA001',
                'autocomplete': 'off',
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Room 100',
                'autocomplete': 'off',
            }),
            'capacity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., 25',
                'min': 1,
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Building A, Floor 2',
            }),
            'env_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
                'role': 'switch',
                'id': 'flexSwitchCheckDefault',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].widget.template_name = 'widgets/checkbox_input.html'
