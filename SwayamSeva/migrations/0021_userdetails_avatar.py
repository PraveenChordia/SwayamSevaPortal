# Generated by Django 3.2.6 on 2022-06-13 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0020_schemes_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images'),
        ),
    ]
