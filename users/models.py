from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date


def validate_age(value):
    today = date.today()
    age = today.year - value.year - \
        ((today.month, today.day) < (value.month, value.day))
    if age < 15:
        raise ValidationError(
            "Vous devez avoir au moins 15 ans pour créer un compte.")


class User(AbstractUser):
    can_be_contacted = models.BooleanField(default=True)
    can_data_be_shared = models.BooleanField(default=False)
    birth_date = models.DateField(validators=[validate_age])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
