# Generated by Django 3.2.6 on 2022-06-13 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0023_remove_userdetails_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='media/profile_images'),
        ),
    ]