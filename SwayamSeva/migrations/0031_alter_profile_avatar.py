# Generated by Django 3.2.6 on 2022-06-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0030_alter_documents_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default.jpg', upload_to='profile_images/'),
        ),
    ]