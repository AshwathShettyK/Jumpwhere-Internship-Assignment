from django import forms
from django.core.exceptions import ValidationError
from designations.models import Designation
from projects.models import Project
from coding.models import Coding
from tools.models import Tool
from .models import Employee, EmployeeProject

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 
            'last_name', 
            'email', 
            'phone', 
            'designation', 
            'professional_summary', 
            'coding_skills', 
            'tools', 
            'status'
        ]
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Enter first name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Enter last name',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Enter email address',
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Optional phone number',
                }
            ),
            'designation': forms.Select(
                attrs={'class': 'form-select form-control-lg'}
            ),
            'professional_summary': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Double click / add bullet lines below...',
                    'rows': 4,
                }
            ),
            'coding_skills': forms.SelectMultiple(
                attrs={
                    'class': 'form-select select2-bootstrap',
                    'multiple': 'multiple',
                }
            ),
            'tools': forms.SelectMultiple(
                attrs={
                    'class': 'form-select select2-bootstrap',
                    'multiple': 'multiple',
                }
            ),
            'status': forms.Select(
                attrs={'class': 'form-select form-control-lg'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate master records that are active & not deleted
        self.fields['designation'].queryset = Designation.objects.filter(status='active', is_deleted=False)
        self.fields['coding_skills'].queryset = Coding.objects.filter(status='active', is_deleted=False)
        self.fields['tools'].queryset = Tool.objects.filter(status='active', is_deleted=False)

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise ValidationError('Email address is required.')

        existing = Employee.all_objects.filter(email__iexact=email, is_deleted=False)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise ValidationError('An employee with this email address already exists.')

        return email


class EmployeeProjectForm(forms.ModelForm):
    class Meta:
        model = EmployeeProject
        fields = ['employee', 'project', 'role']
        widgets = {
            'employee': forms.Select(attrs={'class': 'form-select form-control-lg'}),
            'project': forms.Select(attrs={'class': 'form-select form-control-lg'}),
            'role': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Specify project role (e.g. Lead Frontend Developer)',
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter project mappings to active projects only
        self.fields['project'].queryset = Project.objects.filter(status='active', is_deleted=False)
        self.fields['employee'].queryset = Employee.objects.filter(status='active', is_deleted=False)

    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data.get('employee')
        project = cleaned_data.get('project')

        if employee and project:
            existing = EmployeeProject.all_objects.filter(
                employee=employee,
                project=project,
                is_deleted=False,
            )
            if self.instance.pk:
                existing = existing.exclude(pk=self.instance.pk)

            if existing.exists():
                raise ValidationError('This employee is already mapped to the selected project.')

        return cleaned_data
