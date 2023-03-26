from django.db import models

from operation_fournisseur.models import Fournisseur


class Client(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Suspendu"),
        (3, "Supprimé"),
    ]
    responsable: models.CharField(max_length=128)
    raison_sociale: models.CharField(max_length=128)
    pays: models.CharField(max_length=25)
    ville: models.CharField(max_length=25)
    adresse: models.CharField(max_length=40)
    telephone: models.CharField(max_length=14, null=False)
    email: models.CharField(max_length=128)
    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)

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
    client: models.ForeignKey(Client, on_delete=models.CASCADE)
    numero_compte: models.CharField(max_length=12)
    devise: models.IntegerField(choices=devises)
    status: models.IntegerField(choices=status_values, default=1, null=False)

    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)

    def __str__(self):
        return f"{self.numero_compte} {self.client.raison_sociale}"


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
    type_operation: models.IntegerField(choices=types_operation, null=False)
    compte_client: models.ForeignKey(CompteClient, on_delete=models.CASCADE)
    montant: models.BigIntegerField(null=False)
    taux: models.FloatField(null=True)
    motif: models.CharField(max_length=250, null=True)
    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)


class FactureExpedition(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
    ]
    fournisseur_exp: models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    poids_exp: models.FloatField(null=False)
    slug: models.CharField(max_length=12, null=False)
    carrat_moyen: models.IntegerField()
    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)


class Expedition(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
        (3, "Annulée"),
    ]
    client_exp: models.ForeignKey(Client, on_delete=models.CASCADE)
    status: models.IntegerField(choices=status_values, default=1, null=False)
    facture_exp: models.ForeignKey(FactureExpedition, on_delete=models.CASCADE)


class Vente(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validée"),
        (3, "Annulée"),
    ]
    poids: models.FloatField()
    carrat: models.IntegerField()
    densite: models.FloatField()
    prix_unit_vente: models.BigIntegerField()
    montant: models.BigIntegerField()
    fixing_bourse: models.FloatField()
    discompte: models.FloatField()
    client: models.ForeignKey(Client, on_delete=models.CASCADE)
    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)

