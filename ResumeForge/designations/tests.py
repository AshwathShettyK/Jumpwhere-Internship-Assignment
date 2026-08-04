from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Designation


class DesignationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')
        self.designation = Designation.objects.create(
            designation_name='Software Engineer',
            description='Develops applications',
            status=Designation.STATUS_ACTIVE,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_designation_list_view(self):
        response = self.client.get(reverse('designations:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software Engineer')

    def test_designation_create_view(self):
        response = self.client.post(reverse('designations:create'), {
            'designation_name': 'Product Manager',
            'description': 'Manages products',
            'status': Designation.STATUS_ACTIVE,
        })
        self.assertRedirects(response, reverse('designations:list'))
        self.assertTrue(Designation.objects.filter(designation_name='Product Manager').exists())

    def test_designation_update_view(self):
        response = self.client.post(reverse('designations:edit', kwargs={'pk': self.designation.pk}), {
            'designation_name': 'Lead Engineer',
            'description': 'Leads engineering efforts',
            'status': Designation.STATUS_INACTIVE,
        })
        self.assertRedirects(response, reverse('designations:list'))
        self.designation.refresh_from_db()
        self.assertEqual(self.designation.designation_name, 'Lead Engineer')

    def test_designation_soft_delete(self):
        response = self.client.post(reverse('designations:delete', kwargs={'pk': self.designation.pk}))
        self.assertRedirects(response, reverse('designations:list'))
        self.designation.refresh_from_db()
        self.assertTrue(self.designation.is_deleted)

    def test_duplicate_designation_name(self):
        response = self.client.post(reverse('designations:create'), {
            'designation_name': 'software engineer',
            'description': 'Duplicate name test',
            'status': Designation.STATUS_ACTIVE,
        })
        self.assertEqual(response.status_code, 200)
        response = response.render()
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('A designation with this name already exists.', form.errors['designation_name'])
