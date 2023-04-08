# Generated by Django 4.1.7 on 2023-04-08 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation_client', '0003_remove_operationcompteclient_montant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_clients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='compteclient',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_comptes_clients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expedition',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_expeditions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='factureexpedition',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_factures_expeditions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='operationcompteclient',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_operations_comptes_clients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vente',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_ventes', to=settings.AUTH_USER_MODEL),
        ),
    ]
