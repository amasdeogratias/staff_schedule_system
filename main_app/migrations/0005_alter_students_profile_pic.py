# Generated by Django 3.2.16 on 2023-05-26 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_notificationstaff_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.FileField(upload_to='profile_images'),
        ),
    ]