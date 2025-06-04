from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from apps.teachers.models.teacher import Teacher
from apps.teachers.services.teacher_service import TeacherService

User = get_user_model()


class TeacherServiceTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="profesor1",
            password="testpass123",
            first_name="Carlos",
            last_name="Ruiz",
            email="carlos.ruiz@example.com"
        )
        self.teacher = TeacherService.create_teacher(
            user=self.user,
            document_number="123456789",
            phone="3001234567",
            address="Calle 123"
        )

    def test_create_teacher_success(self):
        self.assertEqual(Teacher.objects.count(), 1)
        self.assertEqual(self.teacher.user.username, "profesor1")
        self.assertEqual(self.teacher.document_number, "123456789")

    def test_create_teacher_duplicate_document_raises_error(self):
        another_user = User.objects.create_user(
            username="profesor2",
            password="testpass456"
        )
        with self.assertRaises(ValidationError):
            TeacherService.create_teacher(
                user=another_user,
                document_number="123456789"
            )

    def test_update_teacher_successfully(self):
        data = {
            'first_name': "Carlos Eduardo",
            'last_name': "Ruiz Gómez",
            'email': "carlos.ed@example.com",
            'document_number': "987654321",
            'phone': "3112223344",
            'address': "Nueva dirección"
        }

        updated = TeacherService.update_teacher(self.teacher, data)
        self.assertEqual(updated.document_number, "987654321")
        self.assertEqual(updated.phone, "3112223344")
        self.assertEqual(updated.user.first_name, "Carlos Eduardo")
        self.assertEqual(updated.user.email, "carlos.ed@example.com")

    def test_get_teacher_by_user(self):
        found = TeacherService.get_by_user(self.user)
        self.assertEqual(found.id, self.teacher.id)

    def test_list_all_teachers(self):
        all_teachers = TeacherService.list_all()
        self.assertEqual(len(all_teachers), 1)

    def test_delete_teacher(self):
        TeacherService.delete_teacher(self.teacher.id)
        self.assertEqual(Teacher.objects.count(), 0)
