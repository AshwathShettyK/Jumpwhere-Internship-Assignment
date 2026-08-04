from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Tool


class ToolTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')
        self.tool = Tool.objects.create(
            tool_name='Docker',
            description='Containerization tool',
            status=Tool.STATUS_ACTIVE,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_tool_list_view(self):
        response = self.client.get(reverse('tools:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Docker')

    def test_tool_create_view(self):
        response = self.client.post(reverse('tools:create'), {
            'tool_name': 'Git',
            'description': 'Version control',
            'status': Tool.STATUS_ACTIVE,
        })
        self.assertRedirects(response, reverse('tools:list'))
        self.assertTrue(Tool.objects.filter(tool_name='Git').exists())

    def test_tool_update_view(self):
        response = self.client.post(reverse('tools:edit', kwargs={'pk': self.tool.pk}), {
            'tool_name': 'Docker Updated',
            'description': 'Updated description',
            'status': Tool.STATUS_INACTIVE,
        })
        self.assertRedirects(response, reverse('tools:list'))
        self.tool.refresh_from_db()
        self.assertEqual(self.tool.tool_name, 'Docker Updated')

    def test_tool_soft_delete(self):
        response = self.client.post(reverse('tools:delete', kwargs={'pk': self.tool.pk}))
        self.assertRedirects(response, reverse('tools:list'))
        self.tool.refresh_from_db()
        self.assertTrue(self.tool.is_deleted)

    def test_duplicate_tool_name(self):
        response = self.client.post(reverse('tools:create'), {
            'tool_name': 'docker',
            'description': 'Duplicate test',
            'status': Tool.STATUS_ACTIVE,
        })
        self.assertEqual(response.status_code, 200)
        response = response.render()
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('A tool with this name already exists.', form.errors['tool_name'])
