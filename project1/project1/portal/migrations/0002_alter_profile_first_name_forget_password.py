# Generated by Django 4.1.5 on 2023-01-20 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=500),
        ),
        migrations.CreateModel(
            name='Forget_Password',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=254)),
                ('status', models.BooleanField()),
                ('token', models.CharField(max_length=150)),
                ('timestamp', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
