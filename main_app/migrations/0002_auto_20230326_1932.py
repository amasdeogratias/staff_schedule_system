# Generated by Django 3.2.18 on 2023-03-26 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='session_end_year',
        ),
        migrations.RemoveField(
            model_name='students',
            name='session_start_year',
        ),
    ]
