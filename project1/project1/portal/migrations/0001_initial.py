# Generated by Django 4.1.5 on 2023-01-13 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('profile_pic', models.ImageField(upload_to='profile')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('nationality', models.CharField(choices=[('india', 'India'), ('pakistan', 'Pakistan'), ('nepal', 'Nepal'), ('bangladesh', 'Bangladesh')], max_length=50)),
                ('passw', models.CharField(max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
