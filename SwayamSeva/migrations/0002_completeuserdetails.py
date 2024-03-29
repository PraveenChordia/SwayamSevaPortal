# Generated by Django 3.2.8 on 2021-12-03 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteUserDetails',
            fields=[
                ('UDid', models.AutoField(primary_key=True, serialize=False)),
                ('F_name', models.CharField(max_length=50)),
                ('M_name', models.CharField(max_length=50, null=True)),
                ('L_name', models.CharField(max_length=50)),
                ('Gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=6)),
                ('DOB', models.DateField()),
                ('Father_name', models.CharField(max_length=100)),
                ('Mother_name', models.CharField(max_length=100)),
                ('Address_L1', models.CharField(max_length=50)),
                ('Address_L2', models.CharField(max_length=50, null=True)),
                ('City', models.CharField(max_length=60)),
                ('State', models.CharField(max_length=60)),
                ('Pincode', models.IntegerField()),
                ('Aadhaar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'CompleteUserDetails',
            },
        ),
    ]
