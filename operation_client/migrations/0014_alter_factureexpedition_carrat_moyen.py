# Generated by Django 4.1.7 on 2023-05-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_client', '0013_ventedetail_achat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factureexpedition',
            name='carrat_moyen',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
