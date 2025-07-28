from django import forms
from django.contrib.auth.models import Group, User
from django.core.exceptions import ValidationError
from apps.teachers.models import teacher


class TeacherForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        label='Password',
        required=False
    )

    class Meta:
        model = teacher
        fields = ['name', 'last_name', 'id_type', 'id_number', 'academic_level',
                  'contract_type', 'academic_area', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Jude'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Bellingham'}),
            'id_type': forms.Select(attrs={'class': 'form-control'}),
            'id_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 1062489657'}),
            'academic_level': forms.Select(attrs={'class': 'form-control'}),
            'contract_type': forms.Select(attrs={'class': 'form-control'}),
            'academic_area': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
                'role': 'switch',
                'id': 'flexSwitchCheckDefault'
            }),
        }
        labels = {
            'academic_level': 'Academic Level',
            'contract_type': 'Contract Type',
            'academic_area': 'Academic Area',
            'is_active': 'Is Active',
            'name': 'Name',
            'last_name': 'Last name',
            'id_type': 'ID',
            'id_number': 'ID Number',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['is_active'].widget.template_name = 'widgets/checkbox_input.html'

    def clean(self):
        cleaned_data = super().clean()
        id_number = cleaned_data.get('id_number')
        if id_number and id_number.startswith('0'):
            raise ValidationError('Invalid ID number, ID cannot start with 0')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if instance.user:
            user = instance.user
            user.username = self.cleaned_data['id_number']
            user.first_name = self.cleaned_data['name']
            user.last_name = self.cleaned_data['last_name']
            if password:
                user.set_password(password)
        else:
            user = User.objects.create_user(
                username=self.cleaned_data['id_number'],
                password=self.cleaned_data['password'],
                first_name=self.cleaned_data['name'],
                last_name=self.cleaned_data['last_name'],
            )
            group = Group.objects.get(name='Teacher')
            user.groups.add(group)
            instance.user = user

        if commit:
            instance.save()
            user.save()
        return instance
