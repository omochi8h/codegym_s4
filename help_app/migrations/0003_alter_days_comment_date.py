# Generated by Django 3.2.7 on 2021-10-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help_app', '0002_alter_houseworks_point'),
    ]

    operations = [
        migrations.AlterField(
            model_name='days_comment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
