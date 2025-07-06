from django.db import models

from apps.users.models import User


class Teacher(models.Model):
    class ID_type(models.TextChoices):
        NATIONAL_ID = 'NID', 'National ID'
        FOREIGN_ID = 'FID', 'Foreign ID Card'
        PASSPORT = 'PASS', 'Passport'
        VISA = 'VISA', 'Visa'

    class Academic_level(models.TextChoices):
        PROFESIONAL = 'PROF', 'Profesional Degree'
        TECHNICAL = 'TECH', 'Technical Training'

    class Contract_type(models.TextChoices):
        TENURED = 'TEN', 'Tenured (Permanent Staff)'
        CONTRACTUAL = 'CON', 'Contract-based Position'

    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_type = models.CharField(
        max_length=10,
        choices= ID_type.choices,
        default=ID_type.NATIONAL_ID)
    id_number = models.CharField(
        max_length=12,
        unique=True)

    academic_level = models.CharField(
        Academic_level.choices,
        max_length=5,
        default=Academic_level.PROFESIONAL)

    contract_type = models.CharField(
        Contract_type.choices,
        max_length=5,
        default=Contract_type.TENURED)

    academic_area = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.academic_area}'

