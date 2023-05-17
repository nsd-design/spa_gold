# Generated by Django 4.1.7 on 2023-05-13 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0033_alter_fixingdetail_type_envoie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achatitems',
            name='carrat_achat',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='achatitems',
            name='poids_achat',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='facturefournisseur',
            name='carrat_moyen',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='facturefournisseur',
            name='poids_total',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='fixing',
            name='fixing_bourse',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AlterField(
            model_name='fixing',
            name='poids_fixe',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
