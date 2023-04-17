from django.db import models
from django.utils import timezone

from operation_fournisseur.models import Fournisseur, Achat
from utilisateurs.models import Utilisateur


class Client(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Suspendu"),
        (3, "Supprimé"),
    ]
    responsable = models.CharField(max_length=128)
    raison_sociale = models.CharField(max_length=128)
    pays = models.CharField(max_length=25)
    ville = models.CharField(max_length=25)
    adresse = models.CharField(max_length=40)
    telephone = models.CharField(max_length=14, null=False, unique=True)
    email = models.CharField(max_length=128, unique=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_clients', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_clients', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.raison_sociale} {self.responsable}"


class CompteClient(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Suspendu"),
        (3, "Supprimé"),
    ]
    devises = [
        (1, "GNF"),
        (2, "USD"),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    numero_compte = models.CharField(max_length=12, unique=True)
    devise = models.IntegerField(choices=devises)
    status = models.IntegerField(choices=status_values, default=1, null=False)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_comptes_clients', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_comptes_clients', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.numero_compte} {self.client}"


class OperationCompteClient(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
        (3, "Annulée"),
    ]
    types_operation = [
        (1, "Paiement"),
        (2, "Avancer"),
        (3, "Entrée"),
        (4, "Sortie"),
    ]
    type_operation = models.IntegerField(choices=types_operation, null=False)
    compte_client = models.ForeignKey(CompteClient, on_delete=models.CASCADE)
    taux = models.FloatField(null=True)
    motif = models.CharField(max_length=250, null=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_operations_comptes_clients', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_operations_comptes_clients', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type_operation} {self.compte_client}"


class FactureExpedition(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
    ]
    fournisseur_exp = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    poids_exp = models.FloatField(null=False)
    slug = models.CharField(max_length=12, null=False)
    carrat_moyen = models.FloatField()
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_factures_expeditions', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_factures_expeditions', null=True, on_delete=models.CASCADE)


class Expedition(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
        (3, "Annulée"),
    ]
    client_exp = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    facture_exp = models.ForeignKey(FactureExpedition, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_expeditions', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_expeditions', null=True, on_delete=models.CASCADE)


class Vente(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
        (3, "Annulée"),
    ]

    types = [
        (1, "Vente par barres"),
        (2, "Vente globale"),
    ]

    fixing_bourse = models.FloatField()
    discount = models.FloatField()
    type = models.SmallIntegerField(choices=types, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_ventes', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_ventes', null=True, on_delete=models.CASCADE)


class VenteDetail(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE)
    poids = models.FloatField()
    carrat = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
