# Generated by Django 5.2 on 2025-05-08 07:40

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="birth_date",
            field=models.DateField(
                blank=True, null=True, validators=[users.models.validate_age]
            ),
        ),
    ]
