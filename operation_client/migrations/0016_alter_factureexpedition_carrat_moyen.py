# Generated by Django 4.1.7 on 2023-05-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_client', '0015_alter_factureexpedition_poids_exp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factureexpedition',
            name='carrat_moyen',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
