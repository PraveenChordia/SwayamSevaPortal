# Generated by Django 3.2.6 on 2022-06-14 06:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0029_alter_documents_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='Uid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Doc_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
