# Generated by Django 4.1.7 on 2023-04-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0018_remove_fixingdetail_achat'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixing',
            name='carrat_moyen',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
