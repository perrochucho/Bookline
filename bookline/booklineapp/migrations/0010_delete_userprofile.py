# Generated by Django 4.2 on 2023-05-18 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booklineapp', '0009_userprofile_user_alter_userprofile_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
