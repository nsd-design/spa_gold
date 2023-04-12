import uuid

from django.db import models

from utilisateurs.models import Utilisateur


class Fournisseur(models.Model):
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
    created_by = models.ForeignKey(Utilisateur, related_name='created_fournisseurs', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_fournisseurs', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.prenom} {self.nom} {self.telephone}"


class Achat(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validé"),
    ]
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    slug = models.UUIDField(max_length=255, default=uuid.uuid4, editable=False, unique=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_achats', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.slug}, {self.fournisseur}"


class AchatItems(models.Model):
    poids_achat = models.FloatField()
    carrat_achat = models.FloatField()
    manquant = models.FloatField(null=True)
    achat = models.ForeignKey(Achat, related_name="achat_achat_items", null=True, blank=True, on_delete=models.CASCADE)


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
    numero_compte_fournis = models.CharField(max_length=12, null=False, unique=True, blank=False)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    devise = models.IntegerField(choices=devises, null=False)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_comptes_fournisseurs', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_comptes_fournisseurs', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.numero_compte_fournis} {self.fournisseur}"


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
    type_operation = models.IntegerField(choices=types_operation, null=False)
    compte_fournis = models.ForeignKey(CompteFournisseur, on_delete=models.CASCADE)
    taux = models.FloatField(null=True)
    motif = models.CharField(max_length=250, null=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_operations_comptes_fournis', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_operations_comptes_fournis', null=True, on_delete=models.CASCADE)


class LotArrivage(models.Model):
    status_values = [
        (1, "Actif"),
        (2, "Clôturé"),
        (3, "Supprimé"),
    ]
    designation = models.CharField(max_length=28, unique=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_lots_arrivages', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_lots_arrivages', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.designation}"


class Attribution(models.Model):
    status_values = [
        (1, "Placée"),
    ]

    nombre_barre = models.IntegerField(null=False)
    poids_achete = models.FloatField(null=True)
    poids_vendu = models.FloatField(null=True)
    poids_restant = models.FloatField(null=True)
    arrivage = models.ForeignKey(LotArrivage, on_delete=models.CASCADE)

    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_attributions', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_attributions', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.arrivage} {self.nombre_barre}"


class Fixing(models.Model):
    status_values = [
        (1, "En cours"),
        (2, "Validé"),
        (3, "Annulé"),
    ]

    poids_fixe = models.FloatField()
    status = models.IntegerField(choices=status_values, default=1, null=False)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    fixing_bourse = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_fixings', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_fixings', null=True, on_delete=models.CASCADE)
