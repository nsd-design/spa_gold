# Generated by Django 4.1.7 on 2023-05-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0028_caisse_fournisseur_caisse_montant_anterieur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='achatitems',
            name='item_used',
            field=models.BooleanField(default=False),
        ),
    ]