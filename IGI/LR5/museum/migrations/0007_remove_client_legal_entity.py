# Generated by Django 5.0.6 on 2024-05-29 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0006_remove_customuser_age_customuser_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='legal_entity',
        ),
    ]
