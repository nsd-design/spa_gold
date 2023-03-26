from django.db import models


class Fournisseur(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Suspendu"),
        (3, "Supprimé"),
    ]
    nom: models.CharField(max_length=30)
    prenom: models.CharField(max_length=40)
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
        return f"{self.prenom} {self.nom} {self.telephone}"


class Achat(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validé"),
    ]
    poids_achat: models.FloatField()
    carrat_achat: models.IntegerField()
    prix_unit_achat: models.BigIntegerField()
    montant_achat: models.BigIntegerField()
    slug: models.CharField(max_length=12, null=False)
    fournisseur: models.ForeignKey(Fournisseur, on_delete=models.DO_NOTHING)
    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)


class CompteFournisseur(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Suspendu"),
        (3, "Supprimé"),
    ]
    devises = [
        (1, "GNF"),
        (2, "USD"),
    ]
    numero_compte_fournis: models.CharField(max_length=12, null=False, unique=True, blank=False)
    fournisseur: models.ForeignKey(Fournisseur, on_delete=models.DO_NOTHING)
    devise: models.IntegerField(choices=devises, null=False)
    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)

    def __str__(self):
        return f"{self.numero_compte_fournis} {self.fournisseur.telephone}"


class OperationCompteFournis(models.Model):
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
    compte_fournis: models.ForeignKey(CompteFournisseur, on_delete=models.DO_NOTHING)
    montant: models.BigIntegerField(null=False)
    taux: models.FloatField(null=True)
    motif: models.CharField(max_length=250, null=True)
    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)

    def __str__(self):
        return f"{self.type_operation} {self.compte_fournis.numero_compte_fournis}"


class LotArrivage(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Clôturé"),
        (3, "Supprimé"),
    ]
    designation: models.CharField(max_length=28)
    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)

    def __str__(self):
        return f"{self.designation} {self.status}"


class Attribution(models.Model):
    status_values = [
        (1, "Placée"),
    ]

    nombre_barre: models.IntegerField(null=False)
    poids_achete: models.FloatField(null=True)
    poids_vendu: models.FloatField(null=True)
    poids_restant: models.FloatField(null=True)
    arrivage: models.ForeignKey(LotArrivage, on_delete=models.DO_NOTHING)

    status: models.IntegerField(choices=status_values, default=1, null=False)
    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)


class Fixing(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validé"),
        (3, "Annulé"),
    ]

    poids_fixe: models.FloatField()
    status: models.IntegerField(choices=status_values, default=1, null=False)
    fournisseur: models.ForeignKey(Fournisseur, on_delete=models.DO_NOTHING)
    fixing_bourse: models.FloatField()

    created_at: models.DateTimeField(auto_now_add=True)
    created_by: models.IntegerField(null=False, default=1)
    updated_at: models.DateTimeField(null=True)
    updated_by: models.IntegerField(null=True)
