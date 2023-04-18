# Generated by Django 4.1.7 on 2023-04-18 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0015_achat_carrat_moyen_achat_poids_total'),
        ('operation_client', '0010_remove_vente_discount_remove_vente_fixing_bourse_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ventedetail',
            name='achat',
        ),
        migrations.RemoveField(
            model_name='ventedetail',
            name='carrat',
        ),
        migrations.RemoveField(
            model_name='ventedetail',
            name='poids',
        ),
        migrations.AddField(
            model_name='ventedetail',
            name='achat_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='operation_fournisseur.achatitems'),
            preserve_default=False,
        ),
    ]