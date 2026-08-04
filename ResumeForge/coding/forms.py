from django import forms

from .models import Coding


class CodingForm(forms.ModelForm):
    class Meta:
        model = Coding
        fields = ['coding_name', 'description', 'status']
        widgets = {
            'coding_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter coding skill name',
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

    def clean_coding_name(self):
        name = self.cleaned_data['coding_name'].strip()
        if not name:
            raise forms.ValidationError('Coding skill name is required.')

        existing = Coding.all_objects.filter(coding_name__iexact=name, is_deleted=False)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise forms.ValidationError('A coding skill with this name already exists.')

        return name
