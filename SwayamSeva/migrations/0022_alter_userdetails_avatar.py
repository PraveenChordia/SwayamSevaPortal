# Generated by Django 3.2.6 on 2022-06-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0021_userdetails_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='avatar',
            field=models.ImageField(default='media/default.jpg', upload_to='media/profile_images'),
        ),
    ]
