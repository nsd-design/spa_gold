# Generated by Django 4.1.7 on 2023-05-25 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0044_fixingdetail_carrat_moyen_restant'),
        ('operation_client', '0022_alter_expedition_achat_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='achat_items',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='operation_fournisseur.achatitems'),
        ),
    ]
