# Generated by Django 3.2.8 on 2021-12-19 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SwayamSeva', '0017_alter_documents_mobile_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documents',
            name='Bank_Acc_no',
            field=models.CharField(max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='documents',
            name='Mobile_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
