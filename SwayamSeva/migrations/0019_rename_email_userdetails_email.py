# Generated by Django 3.2.8 on 2022-05-30 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0018_auto_20211219_1042'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='email',
            new_name='EMAIL',
        ),
    ]
