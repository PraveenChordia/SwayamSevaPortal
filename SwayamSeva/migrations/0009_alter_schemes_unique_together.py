# Generated by Django 3.2.8 on 2021-12-05 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0008_auto_20211204_1752'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='schemes',
            unique_together={('Scheme_Name', 'Aadhaar')},
        ),
    ]