# Generated by Django 4.1.7 on 2023-04-18 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_client', '0009_ventedetail_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vente',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='vente',
            name='fixing_bourse',
        ),
        migrations.RemoveField(
            model_name='vente',
            name='type',
        ),
        migrations.AddField(
            model_name='ventedetail',
            name='type',
            field=models.IntegerField(choices=[(1, 'Vente par barres'), (2, 'Vente globale')], default=20230417),
            preserve_default=False,
        ),
    ]