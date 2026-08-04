from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from designations.models import Designation
from .models import Employee


class EmployeeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.designation = Designation.objects.create(
            designation_name='Software Engineer',
            status=Designation.STATUS_ACTIVE,
        )
        self.client = Client()
        self.client.login(username='testuser', password='password')
        self.employee = Employee.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='555-0100',
            designation=self.designation,
            status=Employee.STATUS_ACTIVE,
            created_by=self.user,
            updated_by=self.user,
        )

    def test_employee_list_view(self):
        response = self.client.get(reverse('employees:list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_employee_create_view(self):
        response = self.client.post(reverse('employees:create'), {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'phone': '555-0200',
            'designation': self.designation.pk,
            'status': Employee.STATUS_ACTIVE,
        })
        self.assertRedirects(response, reverse('employees:list'))
        self.assertTrue(Employee.objects.filter(email='jane.smith@example.com').exists())

    def test_employee_update_view(self):
        response = self.client.post(reverse('employees:edit', kwargs={'pk': self.employee.pk}), {
            'first_name': 'John',
            'last_name': 'Smith',
            'email': 'john.doe@example.com',
            'phone': '555-0101',
            'designation': self.designation.pk,
            'status': Employee.STATUS_INACTIVE,
        })
        self.assertRedirects(response, reverse('employees:list'))
        self.employee.refresh_from_db()
        self.assertEqual(self.employee.last_name, 'Smith')
        self.assertEqual(self.employee.status, Employee.STATUS_INACTIVE)

    def test_employee_soft_delete(self):
        response = self.client.post(reverse('employees:delete', kwargs={'pk': self.employee.pk}))
        self.assertRedirects(response, reverse('employees:list'))
        self.employee.refresh_from_db()
        self.assertTrue(self.employee.is_deleted)

    def test_duplicate_employee_email(self):
        response = self.client.post(reverse('employees:create'), {
            'first_name': 'Duplicate',
            'last_name': 'User',
            'email': 'JOHN.DOE@example.com',
            'phone': '555-0300',
            'designation': self.designation.pk,
            'status': Employee.STATUS_ACTIVE,
        })
        self.assertEqual(response.status_code, 200)
        response = response.render()
        form = response.context['form']
        self.assertTrue(form.errors)
        self.assertIn('An employee with this email address already exists.', form.errors['email'])
