# Generated by Django 4.2 on 2023-05-18 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklineapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='clave',
        ),
    ]
