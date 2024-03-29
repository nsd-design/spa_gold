from django.db import models
from django.utils import timezone

from operation_fournisseur.models import Fournisseur, Achat, AchatItems, LotArrivage
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
    taux = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    montant = models.DecimalField(max_digits=20, decimal_places=2)
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
    poids_exp = models.DecimalField(max_digits=20, decimal_places=2)
    slug = models.CharField(max_length=12, null=False)
    carrat_moyen = models.DecimalField(max_digits=6, decimal_places=2)
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

    types_envoie = [
        (1, "Lot"),
        (2, "Achat"),
        (3, "Details")
    ]

    lot_exp = models.ForeignKey(LotArrivage, null=True, blank=True, on_delete=models.CASCADE)
    client_exp = models.ForeignKey(Client, on_delete=models.CASCADE)
    achat_items = models.OneToOneField(AchatItems, on_delete=models.CASCADE)
    type_envoie = models.IntegerField(choices=types_envoie)
    code_exp = models.BigIntegerField(null=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_expeditions', null=True, on_delete=models.CASCADE)
    updated_at = models.DateField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_expeditions', null=True, on_delete=models.CASCADE)


class Vente(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
        (3, "Annulée"),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_ventes', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_ventes', null=True, on_delete=models.CASCADE)


class VenteDetail(models.Model):

    types = [
        (1, "Vente par barres"),
        (2, "Vente globale"),
    ]

    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    achat_item = models.ForeignKey(AchatItems, on_delete=models.CASCADE)
    type = models.IntegerField(choices=types, null=False)
    achat = models.ForeignKey(Achat, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
