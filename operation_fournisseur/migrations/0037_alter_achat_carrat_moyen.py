# Generated by Django 4.1.7 on 2023-05-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0036_alter_achat_carrat_moyen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat',
            name='carrat_moyen',
            field=models.DecimalField(decimal_places=1, max_digits=6, null=True),
        ),
    ]
