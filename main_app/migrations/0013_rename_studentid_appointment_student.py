# Generated by Django 3.2.16 on 2023-02-27 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_alter_appointment_studentid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='studentId',
            new_name='student',
        ),
    ]
