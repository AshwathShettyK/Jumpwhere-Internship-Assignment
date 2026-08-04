from django import forms
from django.db.utils import OperationalError, ProgrammingError

from employees.models import Employee


def get_employee_queryset():
    try:
        return Employee.objects.filter(is_deleted=False)
    except (OperationalError, ProgrammingError):
        return Employee.objects.none()


class ResumeGeneratorForm(forms.Form):
    employee = forms.ModelChoiceField(
        queryset=get_employee_queryset(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Select Employee',
        empty_label='Choose an employee',
    )
