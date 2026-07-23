from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


class ShortenUrlForm(forms.Form):
    long_url = forms.URLField(
        label="Enter URL",
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
                "placeholder": "https://example.com",
                "required": True,
            }
        ),
    )

    def clean_long_url(self):
        url = self.cleaned_data.get("long_url")
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError:
            raise ValidationError("Please enter a valid URL.")
        return url
