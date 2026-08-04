from django import forms
from django.core.exceptions import ValidationError
from .models import Project
from coding.models import Coding
from tools.models import Tool

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'project_name', 
            'coding_skills', 
            'tools', 
            'description', 
            'role_responsibilities', 
            'start_date', 
            'end_date', 
            'status'
        ]
        widgets = {
            'project_name': forms.TextInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'placeholder': 'Enter project name',
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
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Explain project objective and outcomes...',
                    'rows': 4,
                }
            ),
            'role_responsibilities': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pointers (one per line) describing standard responsibilities...',
                    'rows': 4,
                }
            ),
            'start_date': forms.DateInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'type': 'date',
                }
            ),
            'end_date': forms.DateInput(
                attrs={
                    'class': 'form-control form-control-lg',
                    'type': 'date',
                }
            ),
            'status': forms.Select(
                attrs={'class': 'form-select form-control-lg'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter dropdown to active coding skills and tools only
        self.fields['coding_skills'].queryset = Coding.objects.filter(status='active', is_deleted=False)
        self.fields['tools'].queryset = Tool.objects.filter(status='active', is_deleted=False)

    def clean_project_name(self):
        name = self.cleaned_data.get('project_name', '').strip()
        if not name:
            raise ValidationError('Project name is required.')

        existing = Project.all_objects.filter(project_name__iexact=name, is_deleted=False)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise ValidationError('A project with this name already exists.')

        return name

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date < start_date:
                raise ValidationError({
                    'end_date': 'End Date must be greater than or equal to Start Date.'
                })
        return cleaned_data
