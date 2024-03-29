# Generated by Django 4.1.7 on 2023-04-08 21:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bank', '0002_remove_operationparticulier_montant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compteparticulier',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_comptes_particuliers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='operationparticulier',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_operations_particuliers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='particulier',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='updated_particuliers', to=settings.AUTH_USER_MODEL),
        ),
    ]
