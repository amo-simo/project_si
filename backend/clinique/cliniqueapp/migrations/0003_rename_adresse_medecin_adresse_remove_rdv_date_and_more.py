# Generated by Django 5.0.1 on 2024-01-28 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliniqueapp', '0002_rename_datenaissance_patient_date_de_naissance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medecin',
            old_name='Adresse',
            new_name='adresse',
        ),
        migrations.RemoveField(
            model_name='rdv',
            name='date',
        ),
        migrations.AddField(
            model_name='rdv',
            name='date_de_naissance',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
