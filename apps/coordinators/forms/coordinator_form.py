from django import forms
from apps.coordinators.models.coordinator import Coordinator
from django.utils.translation import gettext_lazy as _


class CoordinatorForm(forms.ModelForm):
    first_name = forms.CharField(
        label=_('Nombres'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
        max_length=150
    )
    last_name = forms.CharField(
        label=_('Apellidos'),
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
        max_length=150
    )
    email = forms.EmailField(
        label=_('Correo electrónico'),
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
    )

    class Meta:
        model = Coordinator
        fields = ['document_number', 'phone', 'address']
        widgets = {
            'document_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número de documento'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Dirección'}),
        }
        labels = {
            'document_number': _('Número de Documento'),
            'phone': _('Teléfono'),
            'address': _('Dirección'),
        }

    def __init__(self, *args, **kwargs):
        # extraemos el usuario asociado
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def clean_document_number(self):
        document_number = self.cleaned_data.get('document_number')
        if Coordinator.objects.filter(document_number=document_number).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(_("Ya existe un coordinador con este número de documento."))
        return document_number

    def save(self, commit=True):
        coordinator = super().save(commit=False)
        user = self.instance.user

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            coordinator.user = user
            coordinator.save()
        return coordinator
