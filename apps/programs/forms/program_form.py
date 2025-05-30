from django import forms
from apps.programs.models.programs import Programs
from django.utils.translation import gettext_lazy as _


class Program_Form(forms.ModelForm):
    class Meta:
        model = Programs
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del programa'}),
        }
        labels = {
            'name': _('Nombre del Programa'),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if Programs.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError(_("Ya existe un programa con este nombre."))
        return name
