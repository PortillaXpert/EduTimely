from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.coordinators.models.coordinator import Coordinator
from apps.coordinators.services.coordinatorservice import CoordinatorService
from django.contrib.auth.models import User



User = get_user_model()


class CoordinatorServiceTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="coordinator1",
            password="securepassword123",
            first_name="Ana",
            last_name="García",
            email="ana.garcia@example.com"
        )
        self.coordinator = CoordinatorService.create_coordinator(
            user=self.user,
            document_number="987654321",
            phone="3216549870"
        )

    def test_create_coordinator_success(self):
        self.assertEqual(Coordinator.objects.count(), 1)
        self.assertEqual(self.coordinator.user.username, "coordinator1")
        self.assertEqual(self.coordinator.document_number, "987654321")

    def test_create_coordinator_duplicate_document_fails(self):
        another_user = User.objects.create_user(
            username="coordinator2",
            password="securepassword456"
        )
        with self.assertRaises(ValueError) as ctx:
            CoordinatorService.create_coordinator(
                user=another_user,
                document_number="987654321",
                phone="1231231234"
            )
        self.assertIn("ya está registrado", str(ctx.exception).lower())

    def test_update_coordinator_successfully(self):
        updated = CoordinatorService.update_coordinator(
            document_number="123456789",
            phone="0987654321",
            first_name="Ana María",
            last_name="González",
            email="ana.mg@example.com"
        )
        self.assertEqual(updated.document_number, "123456789")
        self.assertEqual(updated.phone, "0987654321")
        self.assertEqual(updated.user.first_name, "Ana María")
        self.assertEqual(updated.user.email, "ana.mg@example.com")

    def test_delete_coordinator_successfully(self):
        CoordinatorService.delete_coordinator(self.coordinator.id)
        self.assertFalse(Coordinator.objects.filter(id=self.coordinator.id).exists())

    def test_get_coordinator_by_id(self):
        found = CoordinatorService.get_coordinator_by_id(self.coordinator.id)
        self.assertEqual(found.id, self.coordinator.id)
        self.assertEqual(found.user.username, "coordinator1")

    def test_get_all_coordinators(self):
        coordinators = CoordinatorService.list_all()
        self.assertEqual(len(coordinators), 1)
        self.assertEqual(coordinators[0].document_number, "987654321")
