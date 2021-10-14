# Generated by Django 3.2.7 on 2021-10-06 12:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('help_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parents',
            name='icon',
        ),
        migrations.AlterField(
            model_name='tasks',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
