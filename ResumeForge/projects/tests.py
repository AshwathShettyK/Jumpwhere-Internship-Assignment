from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Project


class ProjectTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')
        self.project = Project.objects.create(
            project_name='HR Portal',
            description='Portal for human resources management',
            status=Project.STATUS_ACTIVE,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_project_list_view(self):
        response = self.client.get(reverse('projects:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'HR Portal')

    def test_project_create_view(self):
        response = self.client.post(reverse('projects:create'), {
            'project_name': 'Resume Builder',
            'description': 'Create and generate resumes',
            'status': Project.STATUS_ACTIVE,
        })
        self.assertRedirects(response, reverse('projects:list'))
        self.assertTrue(Project.objects.filter(project_name='Resume Builder').exists())

    def test_project_update_view(self):
        response = self.client.post(reverse('projects:edit', kwargs={'pk': self.project.pk}), {
            'project_name': 'HR Dashboard',
            'description': 'Updated description',
            'status': Project.STATUS_CLOSED,
        })
        self.assertRedirects(response, reverse('projects:list'))
        self.project.refresh_from_db()
        self.assertEqual(self.project.project_name, 'HR Dashboard')

    def test_project_soft_delete(self):
        response = self.client.post(reverse('projects:delete', kwargs={'pk': self.project.pk}))
        self.assertRedirects(response, reverse('projects:list'))
        self.project.refresh_from_db()
        self.assertTrue(self.project.is_deleted)

    def test_duplicate_project_name(self):
        response = self.client.post(reverse('projects:create'), {
            'project_name': 'hr portal',
            'description': 'Duplicate name test',
            'status': Project.STATUS_ACTIVE,
        })
        self.assertEqual(response.status_code, 200)
        response = response.render()
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('A project with this name already exists.', form.errors['project_name'])
