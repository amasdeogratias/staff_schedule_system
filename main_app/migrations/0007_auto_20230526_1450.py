# Generated by Django 3.2.16 on 2023-05-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_students_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_pic',
            field=models.ImageField(default='', upload_to='profile_images'),
        ),
    ]
