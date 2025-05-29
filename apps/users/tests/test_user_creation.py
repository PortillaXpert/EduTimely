from django.test import TestCase
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from apps.users.forms.login_form import CustomLoginForm
from edutimely_core.constants.roles import COORDINATOR, TEACHER

CustomUser = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        Group.objects.get_or_create(name=COORDINATOR)
        Group.objects.get_or_create(name=TEACHER)

    def test_create_coordinator_user(self):
        user = CustomUser.objects.create_user(
            username='coordinador_test',
            email='coordinador@test.com',
            password='admin1234',
            is_coordinator=True
        )
        self.assertTrue(user.groups.filter(name=COORDINATOR).exists())

    def test_create_teacher_user(self):
        user = CustomUser.objects.create_user(
            username='docente_test',
            email='docente@test.com',
            password='admin1234',
            is_teacher=True
        )
        self.assertTrue(user.groups.filter(name=TEACHER).exists())

class LoginFormTest(TestCase):
    def setUp(self):
        # Crear usuario válido para prueba de login
        self.user = CustomUser.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='admin1234'
        )

    def test_login_form_valid_data(self):
        form = CustomLoginForm(data={'username': 'admin', 'password': 'admin1234'})
        self.assertTrue(form.is_valid())

    def test_login_form_missing_data(self):
        form = CustomLoginForm(data={'username': '', 'password': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)


def test_signal_assigns_group_to_coordinator(self):
    user = CustomUser.objects.create_user(
        username='test_coordinator_signal',
        email='coord_signal@test.com',
        password='admin1234',
        is_coordinator=True
    )
    self.assertTrue(user.groups.filter(name=COORDINATOR).exists())

def test_signal_assigns_group_to_teacher(self):
    user = CustomUser.objects.create_user(
        username='test_teacher_signal',
        email='teacher_signal@test.com',
        password='admin1234',
        is_teacher=True
    )
    self.assertTrue(user.groups.filter(name=TEACHER).exists())
