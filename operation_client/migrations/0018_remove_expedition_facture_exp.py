# Generated by Django 4.1.7 on 2023-05-24 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation_client', '0017_expedition_achat_expedition_achat_items_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expedition',
            name='facture_exp',
        ),
    ]