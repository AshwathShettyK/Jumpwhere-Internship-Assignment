import re
from django.core.exceptions import ValidationError

def validate_password_complexity(value):
    """
    Validates that a password contains at least:
    - 8 characters
    - One uppercase letter
    - One lowercase letter
    - One digit
    - One special character
    """
    if len(value) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.search(r'[A-Z]', value):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', value):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not re.search(r'[0-9]', value):
        raise ValidationError("Password must contain at least one digit.")
    if not re.search(r'[_@$!%*?&+-]', value):
        raise ValidationError("Password must contain at least one special character (_@$!%*?&+-).")

def validate_corporate_email(value):
    """
    Validates that the email follows standard pattern.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, value):
        raise ValidationError("Please provide a valid email address.")
