from django import forms

from .models import Tool


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool_name', 'description', 'status']
        widgets = {
            'tool_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter tool name',
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

    def clean_tool_name(self):
        name = self.cleaned_data['tool_name'].strip()
        if not name:
            raise forms.ValidationError('Tool name is required.')

        existing = Tool.all_objects.filter(tool_name__iexact=name, is_deleted=False)
        if self.instance.pk:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise forms.ValidationError('A tool with this name already exists.')

        return name
