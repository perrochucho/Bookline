# Generated by Django 4.2 on 2023-05-18 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booklineapp', '0006_remove_userprofile_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='NULL', max_length=254),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password1',
            field=models.CharField(default='NULL', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password2',
            field=models.CharField(default='NULL', max_length=128),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default='NULL', max_length=150),
        ),
    ]
