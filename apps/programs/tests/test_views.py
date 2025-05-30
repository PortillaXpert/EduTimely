from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User, Group
from apps.programs.models.programs import Programs

class ProgramViewsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='coord', password='testpass')
        group = Group.objects.create(name='COORDINATOR')
        self.user.groups.add(group)
        self.client.login(username='coord', password='testpass')
        self.program = Programs.objects.create(name="Programación")

    def test_program_list_view(self):
        response = self.client.get(reverse('programs:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Programación")

    def test_program_create_view_post(self):
        response = self.client.post(reverse('programs:create'), {'name': 'Biología'})
        self.assertRedirects(response, reverse('programs:list'))
        self.assertTrue(Programs.objects.filter(name='Biología').exists())

    def test_program_update_view_post(self):
        response = self.client.post(reverse('programs:update', args=[self.program.id]), {'name': 'Ingeniería'})
        self.assertRedirects(response, reverse('programs:list'))
        self.program.refresh_from_db()
        self.assertEqual(self.program.name, 'Ingeniería')

    def test_program_delete_view_post(self):
        response = self.client.post(reverse('programs:delete', args=[self.program.id]))
        self.assertRedirects(response, reverse('programs:list'))
        self.assertFalse(Programs.objects.filter(id=self.program.id).exists())
