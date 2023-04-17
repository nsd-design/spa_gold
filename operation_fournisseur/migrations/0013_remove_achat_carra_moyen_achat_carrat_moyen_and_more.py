# Generated by Django 4.1.7 on 2023-04-17 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0012_achat_carra_moyen_achat_poids_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='achat',
            name='carra_moyen',
        ),
        migrations.AddField(
            model_name='achat',
            name='carrat_moyen',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='achat',
            name='poids_total',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
