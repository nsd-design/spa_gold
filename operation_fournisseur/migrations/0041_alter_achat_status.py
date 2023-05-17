# Generated by Django 4.1.7 on 2023-05-13 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0040_alter_achat_carrat_moyen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achat',
            name='status',
            field=models.IntegerField(choices=[(1, 'En cours'), (2, 'Validé'), (3, 'Cloturé')], default=1),
        ),
    ]
