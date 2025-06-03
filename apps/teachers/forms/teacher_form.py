from django import forms
from apps.teachers.models.teacher import Teacher
from django.contrib.auth import get_user_model

User = get_user_model()


class TeacherForm(forms.ModelForm):
    first_name = forms.CharField(label="Nombre", max_length=150)
    last_name = forms.CharField(label="Apellido", max_length=150)
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = Teacher
        fields = ['document_number', 'phone', 'address', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.user:
            self.fields['first_name'].initial = self.instance.user.first_name
            self.fields['last_name'].initial = self.instance.user.last_name
            self.fields['email'].initial = self.instance.user.email

    def clean_document_number(self):
        document_number = self.cleaned_data['document_number']
        if Teacher.objects.exclude(pk=self.instance.pk).filter(document_number=document_number).exists():
            raise forms.ValidationError("Ya existe un docente con este número de documento.")
        return document_number

    def save(self, commit=True):
        teacher = super().save(commit=False)

        # Guardar datos del usuario asociado
        if self.user:
            user = teacher.user
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.email = self.cleaned_data['email']
            user.save()

        if commit:
            teacher.save()
        return teacher
