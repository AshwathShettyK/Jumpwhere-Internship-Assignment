from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .validators import validate_password_complexity, validate_corporate_email

class HRLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter username',
                'autocomplete': 'username',
            }
        ),
        max_length=150,
        label='Username',
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter password',
                'autocomplete': 'current-password',
            }
        ),
        label='Password',
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='Remember Me',
    )

class HRRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        validators=[validate_corporate_email],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter email address',
                'autocomplete': 'email',
            }
        ),
        label='Email Address',
    )

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['username', 'password1', 'password2']:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['class'] = 'form-control form-control-lg'
                if field_name == 'username':
                    self.fields[field_name].widget.attrs['placeholder'] = 'Choose a username'
                elif field_name == 'password1':
                    self.fields[field_name].widget.attrs['placeholder'] = 'Create a secure password'
                    # Apply password complexity validator
                    self.fields[field_name].validators.append(validate_password_complexity)
                elif field_name == 'password2':
                    self.fields[field_name].widget.attrs['placeholder'] = 'Confirm password'

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email:
            if User.objects.filter(email=email).exists():
                raise ValidationError("An account with this email address already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip().lower()
        if username:
            if User.objects.filter(username=username).exists():
                raise ValidationError("This username is already taken.")
        return username
