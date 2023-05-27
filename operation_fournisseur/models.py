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
        (3, "Cloturé"),
    ]
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    slug = models.UUIDField(max_length=255, default=uuid.uuid4, editable=False, unique=True)
    poids_total = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    carrat_moyen = models.FloatField(null=True)
    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_achats', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fournisseur} ID Achat {self.id}"


class AchatItems(models.Model):
    poids_achat = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    carrat_achat = models.DecimalField(max_digits=6, decimal_places=2)
    manquant = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    achat = models.ForeignKey(Achat, related_name="achat_achat_items", null=True, blank=True, on_delete=models.CASCADE)
    item_used = models.BooleanField(default=False)

    def __str__(self):
        return f"id = {self.id}, poids = {self.poids_achat}, carrat = {self.carrat_achat}, achat = {self.achat}"


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
    taux = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    montant = models.DecimalField(max_digits=20, decimal_places=2)
    solde_anterieur = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
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

    arrivage = models.ForeignKey(LotArrivage, on_delete=models.CASCADE)
    achat = models.ForeignKey(Achat, related_name='achat_attribution', on_delete=models.CASCADE)

    status = models.IntegerField(choices=status_values, default=1, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_attributions', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_attributions', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.arrivage}"


class Fixing(models.Model):

    status_fixing = [
        (1, "En attente"),
        (2, "Validé"),
        (3, "Annulé"),
    ]

    poids_fixe = models.DecimalField(max_digits=20, decimal_places=2)
    fixing_bourse = models.DecimalField(max_digits=20, decimal_places=2)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    discompte = models.DecimalField(max_digits=6, decimal_places=1)
    status = models.IntegerField(choices=status_fixing, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_fixings', null=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(null=True)
    updated_by = models.ForeignKey(Utilisateur, related_name='updated_fixings', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Poids fixe: {self.poids_fixe}, Fournisseur: {self.fournisseur}"


class FixingDetail(models.Model):
    types_envoie = [
        (1, "Par barre"),
        (2, "Global"),
        (3, "Par Poids"),
    ]
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE, null=True, blank=True)
    achat_items = models.BigIntegerField(null=True, blank=True, unique=True)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True, blank=True)
    fixing = models.ForeignKey(Fixing, on_delete=models.CASCADE, null=True, blank=True)
    type_envoie = models.IntegerField(choices=types_envoie)
    poids_select = models.DecimalField(max_digits=18, decimal_places=2, null=True)
    ordre_validation = models.BigIntegerField(null=True, blank=True)
    carrat_moyen_restant = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_fixing_detail', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Achat: {self.achat}, Poids: {self.poids_select}"


class FactureFournisseur(models.Model):
    fixing = models.ForeignKey(Fixing, on_delete=models.CASCADE)
    achat = models.ForeignKey(Achat, on_delete=models.CASCADE)
    poids_total = models.DecimalField(max_digits=20, decimal_places=2)
    carrat_moyen = models.DecimalField(max_digits=6, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_by_facture_fournisseur', null=True, blank=True, on_delete=models.CASCADE)


class Caisse(models.Model):
    type_operation = [
        (1, "Entrée"),
        (2, "Sortie"),
        (3, "Retour en caisse"),
        (4, "Décaissement"),
    ]

    devises = [
        (1, "GNF"),
        (2, "USD"),
    ]

    operation = models.IntegerField(choices=type_operation)
    montant = models.DecimalField(max_digits=20, decimal_places=2)
    devise = models.IntegerField(choices=devises)
    motif = models.CharField(max_length=255)
    fournisseur = models.ForeignKey(Fournisseur, null=True, on_delete=models.CASCADE)
    montant_anterieur = models.DecimalField(max_digits=20, decimal_places=2)
    representant = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Utilisateur, related_name='created_by_caisse', null=True, blank=True,
                                   on_delete=models.CASCADE)
