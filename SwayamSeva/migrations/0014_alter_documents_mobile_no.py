# Generated by Django 3.2.8 on 2021-12-19 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0013_alter_userdetails_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='Mobile_no',
            field=models.IntegerField(null=True),
        ),
    ]