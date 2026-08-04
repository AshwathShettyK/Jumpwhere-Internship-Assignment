from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Coding


class CodingTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.client = Client()
        self.client.login(username='testuser', password='password')
        self.coding = Coding.objects.create(
            coding_name='Python',
            description='Python programming',
            status=Coding.STATUS_ACTIVE,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_coding_list_view(self):
        response = self.client.get(reverse('coding:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python')

    def test_coding_create_view(self):
        response = self.client.post(reverse('coding:create'), {
            'coding_name': 'JavaScript',
            'description': 'Frontend skill',
            'status': Coding.STATUS_ACTIVE,
        })
        self.assertRedirects(response, reverse('coding:list'))
        self.assertTrue(Coding.objects.filter(coding_name='JavaScript').exists())

    def test_coding_update_view(self):
        response = self.client.post(reverse('coding:edit', kwargs={'pk': self.coding.pk}), {
            'coding_name': 'Python Updated',
            'description': 'Updated description',
            'status': Coding.STATUS_INACTIVE,
        })
        self.assertRedirects(response, reverse('coding:list'))
        self.coding.refresh_from_db()
        self.assertEqual(self.coding.coding_name, 'Python Updated')

    def test_coding_soft_delete(self):
        response = self.client.post(reverse('coding:delete', kwargs={'pk': self.coding.pk}))
        self.assertRedirects(response, reverse('coding:list'))
        self.coding.refresh_from_db()
        self.assertTrue(self.coding.is_deleted)

    def test_duplicate_coding_name(self):
        response = self.client.post(reverse('coding:create'), {
            'coding_name': 'python',
            'description': 'Duplicate test',
            'status': Coding.STATUS_ACTIVE,
        })
        self.assertEqual(response.status_code, 200)
        response = response.render()
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('A coding skill with this name already exists.', form.errors['coding_name'])

    def test_coding_soft_delete_excludes_from_queryset(self):
        response = self.client.post(reverse('coding:delete', kwargs={'pk': self.coding.pk}))
        self.assertRedirects(response, reverse('coding:list'))
        self.coding.refresh_from_db()
        self.assertTrue(self.coding.is_deleted)
        self.assertFalse(Coding.objects.filter(pk=self.coding.pk).exists())
        self.assertTrue(Coding.all_objects.filter(pk=self.coding.pk).exists())
