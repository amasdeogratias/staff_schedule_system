# Generated by Django 3.2.15 on 2023-02-10 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffs',
            old_name='department',
            new_name='department_id',
        ),
    ]