# Generated by Django 5.0.1 on 2024-01-28 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliniqueapp', '0003_rename_adresse_medecin_adresse_remove_rdv_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rdv',
            old_name='date_de_naissance',
            new_name='date',
        ),
    ]
