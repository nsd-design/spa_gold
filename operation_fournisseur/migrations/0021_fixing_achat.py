# Generated by Django 4.1.7 on 2023-04-23 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation_fournisseur', '0020_fixing_discompte_fixing_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixing',
            name='achat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='operation_fournisseur.achat'),
            preserve_default=False,
        ),
    ]
