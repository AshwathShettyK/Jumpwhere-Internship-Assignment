from django import forms


class SearchForm(forms.Form):
    word = forms.CharField(
        label="Search word",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter an English word",
                "required": True,
            }
        ),
    )
