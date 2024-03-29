# Generated by Django 4.1.7 on 2023-04-10 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation_fournisseur', '0004_alter_achat_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribution',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_attributions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fixing',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_fixings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_fournisseurs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='operationcomptefournis',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_operations_comptes_fournis', to=settings.AUTH_USER_MODEL),
        ),
    ]
