# Generated by Django 4.1.7 on 2023-04-27 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0024_remove_fixing_achat_remove_fixing_carrat_moyen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fixingdetail',
            name='achat',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation_fournisseur.achat'),
        ),
        migrations.AlterField(
            model_name='fixingdetail',
            name='achat_items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation_fournisseur.achatitems'),
        ),
        migrations.AlterField(
            model_name='fixingdetail',
            name='fixing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation_fournisseur.fixing'),
        ),
        migrations.AlterField(
            model_name='fixingdetail',
            name='fournisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operation_fournisseur.fournisseur'),
        ),
    ]
