from django import forms

from .models import Designation


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = ['designation_name', 'description', 'status']
        widgets = {
            'designation_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter designation name',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Optional description',
                    'rows': 4,
                }
            ),
            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }

    def clean_designation_name(self):
        name = self.cleaned_data['designation_name'].strip()
        if not name:
            raise forms.ValidationError('Designation name is required.')

        existing = Designation.all_objects.filter(designation_name__iexact=name, is_deleted=False)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise forms.ValidationError('A designation with this name already exists.')

        return name
