# Generated by Django 3.2.8 on 2021-12-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0012_userdetails_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]