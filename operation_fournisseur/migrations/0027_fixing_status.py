# Generated by Django 4.1.7 on 2023-05-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0026_fixingdetail_poids_select'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixing',
            name='status',
            field=models.IntegerField(choices=[(1, 'En attente'), (2, 'Validé'), (3, 'Annulé')], default=1),
        ),
    ]
