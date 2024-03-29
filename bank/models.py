from django.db import models

from utilisateurs.models import Utilisateur


class Particulier(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Suspendu"),
        (3, "Supprimé"),
    ]
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=40)
    pays = models.CharField(max_length=25)
    ville = models.CharField(max_length=25)
    adresse = models.CharField(max_length=40)
    telephone = models.CharField(max_length=14, null=False, unique=True)
    email = models.CharField(max_length=128, unique=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_particuliers', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_particuliers', null=True, on_delete=models.CASCADE)


class CompteParticulier(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Suspendu"),
        (3, "Supprimé"),
    ]
    devises = [
        (1, "GNF"),
        (2, "USD"),
    ]
    numero_compte_part = models.CharField(max_length=12, null=False, unique=True, blank=False)
    particulier = models.ForeignKey(Particulier, on_delete=models.CASCADE)
    devise = models.IntegerField(choices=devises, null=False)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_comptes_particuliers', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_comptes_particuliers', null=True, on_delete=models.CASCADE)


class OperationParticulier(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
        (3, "Annulée"),
    ]
    types_operation = [
        (1, "Depôt"),
        (2, "Retrait"),
        (3, "Transfert"),
    ]
    type_operation = models.IntegerField(choices=types_operation, null=False)
    compte_particulier = models.ForeignKey(CompteParticulier, on_delete=models.CASCADE)
    taux = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    motif = models.CharField(max_length=250, null=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_operations_particuliers', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_operations_particuliers', null=True, on_delete=models.CASCADE)
