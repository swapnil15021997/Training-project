# Generated by Django 4.1.5 on 2023-01-18 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationform',
            name='fname',
            field=models.CharField(max_length=500),
        ),
    ]
