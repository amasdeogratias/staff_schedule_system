# Generated by Django 3.2.18 on 2023-03-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_blocks'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='staff_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
