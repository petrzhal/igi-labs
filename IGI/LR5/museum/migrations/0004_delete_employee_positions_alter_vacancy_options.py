# Generated by Django 5.0.6 on 2024-05-28 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0003_alter_bonus_options_alter_company_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Employee_positions',
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
    ]