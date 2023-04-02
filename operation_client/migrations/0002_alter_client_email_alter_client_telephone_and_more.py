# Generated by Django 4.1.7 on 2023-04-01 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='telephone',
            field=models.CharField(max_length=14, unique=True),
        ),
        migrations.AlterField(
            model_name='compteclient',
            name='numero_compte',
            field=models.CharField(max_length=12, unique=True),
        ),
    ]
