from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from designations.models import Designation
from employees.models import Employee, EmployeeProject
from projects.models import Project


class ResumeGeneratorTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='password')
        self.designation = Designation.objects.create(designation_name='Developer', status=Designation.STATUS_ACTIVE)
        self.project = Project.objects.create(project_name='Resume Forge', status=Project.STATUS_ACTIVE)
        self.client = Client()
        self.client.login(username='testuser', password='password')
        self.employee = Employee.objects.create(
            first_name='Alice',
            last_name='Smith',
            email='alice.smith@example.com',
            designation=self.designation,
            status=Employee.STATUS_ACTIVE,
            created_by=self.user,
            updated_by=self.user,
        )
        self.assignment = EmployeeProject.objects.create(
            employee=self.employee,
            project=self.project,
            role='Lead Developer',
            created_by=self.user,
            updated_by=self.user,
        )

    def test_resume_generator_page_loads(self):
        response = self.client.get(reverse('resume_generator:generate'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Resume Generator')

    def test_resume_preview_contains_employee_and_project(self):
        response = self.client.post(reverse('resume_generator:generate'), {
            'employee': self.employee.pk,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice Smith')
        self.assertContains(response, 'Resume Forge')
        self.assertContains(response, 'Lead Developer')

    def test_resume_word_download(self):
        response = self.client.get(reverse('resume_generator:download', kwargs={'pk': self.employee.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response['Content-Type'],
            'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )
        self.assertIn('attachment; filename="Resume_Alice_Smith.docx"', response['Content-Disposition'])
        self.assertTrue(response.content.startswith(b'PK'))

    def test_resume_pdf_download(self):
        response = self.client.get(reverse('resume_generator:download_pdf', kwargs={'pk': self.employee.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn('attachment; filename="Resume_Alice_Smith.pdf"', response['Content-Disposition'])
        self.assertTrue(response.content.startswith(b'%PDF'))

    def test_resume_excludes_deleted_assignments(self):
        self.assignment.is_deleted = True
        self.assignment.save(update_fields=['is_deleted', 'updated_at'])

        response = self.client.post(reverse('resume_generator:generate'), {
            'employee': self.employee.pk,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Alice Smith')
        self.assertContains(response, 'No project assignments available.')
        self.assertNotContains(response, 'Resume Forge')
