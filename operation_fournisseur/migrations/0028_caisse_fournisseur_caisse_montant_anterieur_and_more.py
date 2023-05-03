# Generated by Django 4.1.7 on 2023-05-03 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0027_fixing_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='caisse',
            name='fournisseur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='operation_fournisseur.fournisseur'),
        ),
        migrations.AddField(
            model_name='caisse',
            name='montant_anterieur',
            field=models.DecimalField(decimal_places=2, default=20232017, max_digits=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='caisse',
            name='operation',
            field=models.IntegerField(choices=[(1, 'Entrée'), (2, 'Sortie'), (3, 'Retour en caisse'), (4, 'Décaissement')]),
        ),
    ]
