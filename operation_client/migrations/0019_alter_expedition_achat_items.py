# Generated by Django 4.1.7 on 2023-05-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation_client', '0018_remove_expedition_facture_exp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expedition',
            name='achat_items',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]