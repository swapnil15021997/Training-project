# Generated by Django 4.1.5 on 2023-01-20 07:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0002_alter_profile_first_name_forget_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forget_password',
            name='user',
        ),
        migrations.AddField(
            model_name='forget_password',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
