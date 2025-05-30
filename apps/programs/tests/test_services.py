from django.test import TestCase
from apps.programs.models.programs import Programs
from apps.programs.services.services import Services
from django.core.exceptions import ValidationError

class ProgramServiceTestCase(TestCase):

    def test_create_program_success(self):
        program = Services.create_program(name="Ingeniería de Software")
        self.assertEqual(program.name, "Ingeniería de Software")
        self.assertEqual(Programs.objects.count(), 1)

    def test_create_program_duplicate(self):
        Services.create_program(name="Análisis y Desarrollo")
        with self.assertRaises(ValidationError):
            Services.create_program(name="Análisis y Desarrollo")

    def test_update_program_success(self):
        program = Services.create_program(name="Contabilidad")
        updated = Services.update_program(program.id, name="Contaduría Pública")
        self.assertEqual(updated.name, "Contaduría Pública")

    def test_update_program_duplicate_name(self):
        Services.create_program(name="Sistemas")
        program2 = Services.create_program(name="Mecánica")
        with self.assertRaises(ValidationError):
            Services.update_program(program2.id, name="Sistemas")

    def test_delete_program(self):
        program = Services.create_program(name="Marketing")
        Services.delete_program(program.id)
        self.assertEqual(Programs.objects.count(), 0)
