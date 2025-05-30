from django import forms
from apps.environments.models.environment import Environment
from django.utils.translation import gettext_lazy as _


class EnvironmentForm(forms.ModelForm):
    class Meta:
        model = Environment
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del ambiente'}),
        }
        labels = {
            'name': _('Nombre del Ambiente'),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Environment.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(_("Ya existe un ambiente con este nombre."))
        return name
