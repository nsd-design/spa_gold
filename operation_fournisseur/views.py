import decimal
import json
import random
from datetime import datetime

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Sum, Count
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication

from utilisateurs.models import Utilisateur
from .serializers import *
from django.core import serializers


class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']

    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        """Create new Fournisseur"""
        user = self.request.user
        print("User est :", user)
        # serializer.save(created_by=user)
        serializer.save()

    # @action(detail=True, methods=['PUT'])
    # def update(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

    def perform_update(self, serializer):
        user = self.request.user
        date_time = datetime.now()
        # serializer.save(updated_by=user, updated_at=date_time)
        serializer.save(updated_at=date_time)

    @action(detail=True, methods=['POST'])
    def create_fournisseur(self, request, pk=None):
        print(request.data)

        # if 'telephone' in request.data:
        #     fournisseur = Fournisseur.objects.get(id=pk)
        #     user = Utilisateur.objects.get(id=1)
        #     print("User", user.username)
        #     print("Fournisseur ", fournisseur.nom, " ", fournisseur.prenom)
        #
        #     response = {"message": "Succès"}
        #     return Response(response, status=status.HTTP_200_OK)
        # else:
        #     response = {"message": "Numero de telephone manquant"}
        #     return Response(response, status=status.HTTP_400_BAD_REQUEST)


class AchatViewSet(viewsets.ModelViewSet):
    queryset = Achat.objects.all()
    serializer_class = AchatSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']

    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        """Effectuer un achat"""
        user = self.request.user
        # serializer.save(created_by=user)
        serializer.save()

    def get_queryset(self):
        queryset = Achat.objects.all()

        id_fournisseur = self.request.query_params.get("id_fournisseur")
        if id_fournisseur is not None:
            achats_by_fournisseur = queryset.filter(fournisseur=id_fournisseur, status=2)
            return achats_by_fournisseur

            # try:
            #     achats_du_fournisseur = queryset.filter(fournisseur=id_fournisseur)
            #     achats_pas_dans_fixing_detail = []
            #     # print("Id fournisseur =", id_fournisseur)
            #
            #     poids_total_achat_sup = True
            #     for achat in achats_du_fournisseur:
            #         # Recuperer les Achat ne trouvant pas dans fixing detail
            #         # if not FixingDetail.objects.filter(achat=achat, type_envoie=2).exists():
            #             # achats_pas_dans_fixing_detail.append(achat)
            #             # print("Achat pas dans fixing detail", achats_pas_dans_fixing_detail)
            #             # print("Achat a chercher dans Fixing detail =", achat)
            #
            #         if FixingDetail.objects.filter(achat=achat, type_envoie=3).exists():
            #             print("Achat trouvé dans Fixing detail =", achat)
            #             print("Poids total Achat trouvé dans Fixing detail =", achat.poids_total)
            #             achats_dans_fixing_detail = FixingDetail.objects.filter(achat=achat, type_envoie=3)
            #             somme_poids_achat = achats_dans_fixing_detail.aggregate(somme_poids=Sum('poids_select'))
            #             print("Achat :", achats_dans_fixing_detail, "Somme poids =", somme_poids_achat)
            #             if somme_poids_achat['somme_poids'] is not None:
            #                 if achat.poids_total > somme_poids_achat['somme_poids']:
            #                     print("Somme Poids dans comparaison =", somme_poids_achat['somme_poids'])
            #                     print("Poids total Achat dans comparaison =", achat.poids_total)
            #                     achats_pas_dans_fixing_detail.append(achat)
            #
            #         elif not FixingDetail.objects.filter(achat=achat, type_envoie=2).exists():
            #             achats_pas_dans_fixing_detail.append(achat)
            #
            #     print("Achats pas dans fixing details", achats_pas_dans_fixing_detail)
            #     return achats_pas_dans_fixing_detail
            #
            # except IndexError:
            #     return None

        # Recuperer les achats par Slug
        slug = self.request.query_params.get('slug')
        if slug:
            queryset = queryset.filter(slug=slug)
            return queryset

        """ Recuperer les achats d'après une periode
            definie a travers start_date et end_date """

        start_date = self.request.query_params.get('startDate')
        end_date = self.request.query_params.get('endDate')
        if start_date:
            if start_date != 'undefined' and start_date != '':
                # Converting start date
                date_debut = float(start_date) / 1000
                date_debut_to_local_date = datetime.fromtimestamp(date_debut).date()

                if not end_date == 'undefined' and not end_date == '':
                    # Converting end date
                    date_fin = datetime.fromtimestamp(float(end_date) / 1000).astimezone()
                    qs = queryset.filter(created_at__gte=date_debut_to_local_date,
                                         created_at__lt=date_fin).select_related('fournisseur')
                    # print("Resultat QS", qs)
                    return qs
                elif date_debut_to_local_date:
                    qs = queryset.filter(created_at__date=date_debut_to_local_date).select_related('fournisseur')
                    return qs
        return queryset

    def perform_update(self, serializer):
        date_time = timezone.now()
        req = self.request.query_params
        req_data = self.request.data
        # serializer.save(updated_by=self.request.user, updated_at=date_time)
        serializer.save(updated_at=date_time)


class AchatItemsViewSet(viewsets.ModelViewSet):
    queryset = AchatItems.objects.all()
    serializer_class = AchatItemsSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']

    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        user = self.request.user
        print("user =", user)

        # serializer.save(achat=achat)
        serializer.save()

    def get_queryset(self):
        queryset = AchatItems.objects.all()

        # id_achat = self.request.query_params.get('id_achat')
        id_fournisseur = self.request.query_params.get('id_fournisseur')
        id_achat = 0
        if id_fournisseur:
            try:
                # print("Id fournisseur", id_fournisseur)
                achat_encours = Achat.objects.filter(fournisseur=id_fournisseur, status=1)
                # print("Id achat en cours", achat_encours)
                id_achat = achat_encours[0].id
            except IndexError:
                msg = {"message": "Fournisseur introuvable"}
                return None

            try:

                achat_items = AchatItems.objects.filter(achat=id_achat, item_used=False)
                # print("try achat items", achat_items)
                return achat_items
            except IndexError:
                print("Aucun item pour cet achat")
                msg = {"message": "Aucun item pour cet achat"}
                return None
        return queryset

    @action(detail=True, methods=['GET'])
    def get_achat_items_by_achat(self, request, pk=None, *args, **kwargs):

        # # Recuperer les AchataItems qui ne se trouvent pas dans FixingDetail
        # # en se basant sur l'id de l'achat
        # id_achat = self.request.query_params.get('id_achat')
        if pk is not None:
            try:
                achat_items_all = AchatItems.objects.filter(achat=pk)

                achat_items_pas_dans_fixing_detail = []
                try:
                    achats = FixingDetail.objects.filter(achat=pk).values('achat_id', 'type_envoie')
                    type_envoie = achats[0]['type_envoie']
                    if type_envoie == 3:
                        somme_poids = achats.aggregate(somme_poids=Sum('poids_select'))['somme_poids']
                        response = {
                            "data": [],
                            "type_envoie": type_envoie,
                            "somme_poids": somme_poids
                        }
                        return Response(response, status=status.HTTP_200_OK)

                except IndexError:
                    type_envoie = 0

                for achat_item in achat_items_all:
                    # Vérifier si l'item n'existe pas dans FixingDetail
                    # Et puis l'ajouter dans le tableau
                    if not FixingDetail.objects.filter(achat_items=achat_item.id).exists():
                        instance = AchatItemsSerializer(achat_item)
                        achat_items_pas_dans_fixing_detail.append(instance.data)
                response = {
                    "data": achat_items_pas_dans_fixing_detail,
                    "type_envoie": type_envoie
                }
                return Response(response, status=status.HTTP_200_OK)
            except IndexError:
                response = {"message": "Auccune barre trouvée dans cet Achat"}
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                response = {"message": "l'id doit etre un entier"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def achat_items_by_achat(self, request, pk, *args, **kwargs):
        if pk is not None:
            try:
                achat_items = AchatItems.objects.filter(achat=pk)
                instances = AchatItemsSerializer(achat_items, many=True)
                return Response(instances.data, status=status.HTTP_200_OK)
            except IndexError:
                response = {"message": "Aucune barre attribuée à cet achat"}
                return Response(response, status=status.HTTP_404_NOT_FOUND)

    def perform_update(self, serializer):
        # id_item = self.request.query_params('')
        datas = self.request.data
        print(datas)
        date_time = timezone.now()
        # req = self.request.query_params
        # req_data = self.request.data
        # serializer.save(updated_by=self.request.user, updated_at=date_time)
        serializer.save(updated_at=date_time)


class CompteFournisseurViewSet(viewsets.ModelViewSet):
    queryset = CompteFournisseur.objects.all()
    serializer_class = CompteFournisseurSerializer

    def get_queryset(self):
        comptes_fournisseurs = CompteFournisseur.objects.all()
        id_fournisseur = self.request.query_params.get('fournisseur')

        if id_fournisseur:
            compte_by_fournisseur = comptes_fournisseurs.filter(fournisseur=id_fournisseur)
            return compte_by_fournisseur

        return comptes_fournisseurs


class OperationCompteFournisViewSet(viewsets.ModelViewSet):
    queryset = OperationCompteFournis.objects.all()
    serializer_class = OperationCompteFournisSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class LotArrivageViewSet(viewsets.ModelViewSet):
    queryset = LotArrivage.objects.all()
    serializer_class = LotArrivageSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']

    @action(detail=True, methods=['GET'])
    def get_achat_items(self, request, pk, *args, **kwargs):
        if pk is not None:
            # Rechercher le Lot d'id = pk
            lot = get_object_or_404(LotArrivage, pk=pk)
            try:
                attributions = Attribution.objects.filter(arrivage=lot)
                achats_attribues = attributions.values('achat')

                # Tableau devant recevoir l'id des achats trouvés dans le Lot
                id_achats = []
                for achat in achats_attribues:
                    id_achats.append(achat['achat'])
                print("Tab id achats", id_achats)

                # Recuperer les items de chaque Achat trouvé dans AchatItems
                items_by_achat = AchatItems.objects.filter(achat__in=id_achats)

                # Serialisé le resultat de la requete 'items_by_achat' pour pouvoir l'envoyer
                serialized = AchatItemsSerializer(items_by_achat, many=True)
                response = {"data": serialized.data}
                return Response(response, status.HTTP_200_OK)
            except IndexError:
                response = {"message": "Aucun achat attribué à ce Lot"}
                return Response(response, status.HTTP_404_NOT_FOUND)


class AttributionViewSet(viewsets.ModelViewSet):
    queryset = Attribution.objects.filter()
    serializer_class = AttributionSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class FixingViewSet(viewsets.ModelViewSet):
    queryset = Fixing.objects.all()
    serializer_class = FixingSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class FixingDetailViewSet(viewsets.ModelViewSet):
    queryset = FixingDetail.objects.all()
    serializer_class = FixingDetailSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']

    def perform_update(self, serializer):
        datas = self.request.data
        print(datas)
        date_time = timezone.now()
        # serializer.save(updated_by=self.request.user, updated_at=date_time)
        serializer.save(updated_at=date_time)

    @action(detail=True, methods=['POST'])
    def create_fixing_detail(self, request, pk=None, *args, **kwargs):
        serializer = FixingDetailSerializer(data=request.data, many=True)

        if serializer.is_valid():
            print("Id achat", serializer.data[0]['achat']['id'])
            id_achat = int(serializer.data[0]['achat']['id'])
            achat_cloture = False
            ordre_validation = random.randint(1, 9999999999)
            print("Ordere de validation genere", ordre_validation)
            for fixing_detail in serializer.validated_data:
                FixingDetail.objects.create(
                    achat=fixing_detail['achat'], achat_items=fixing_detail['achat_items'],
                    fournisseur=fixing_detail['fournisseur'], fixing=fixing_detail['fixing'],
                    type_envoie=fixing_detail['type_envoie'],
                    ordre_validation=ordre_validation,
                    created_by=fixing_detail['created_by']
                )

            # Recuperer l'id des AchatItems pour calculer leur POIDS => 'poids_achat'
            id_achat_items = FixingDetail.objects.filter(achat=id_achat).values('achat_items').exclude(achat_items=None)
            print("tab id achat items", id_achat_items)
            achat_items = AchatItems.objects.filter(id__in=id_achat_items)
            somme_poid_achat_items = achat_items.aggregate(somme=Sum('poids_achat'))['somme']
            print("Somme poids achata items", somme_poid_achat_items)

            if somme_poid_achat_items is not None:
                # Si le poids des achats items est egal au poids total de l'achat
                # On cloture l'achat
                achat = Achat.objects.get(id=id_achat)
                if decimal.Decimal(somme_poid_achat_items) == decimal.Decimal(achat.poids_total):
                    achat.status = 3
                    date_time = timezone.now()
                    achat.updated_by = request.user
                    achat.updated_at = date_time
                    achat.save()
                    achat_cloture = True
            response = {
                "somme_poids_achat_items": somme_poid_achat_items,
                "poids_total_achat": achat.poids_total,
                "achat_cloture": achat_cloture,
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        ordre_validation = random.randint(1, 9999999999)
        serializer.save(ordre_validation=ordre_validation)
        type_envoie = serializer.data['type_envoie']
        poids_total_achat = decimal.Decimal(serializer.data['achat']['poids_total'])
        print(poids_total_achat)

        if type_envoie == 3:
            # Poids
            fixing_details = FixingDetail.objects.filter(type_envoie=3, achat=serializer.data['achat']['id'])
            sum_poids_fixing = fixing_details.aggregate(somme_poids_select=Sum('poids_select'))['somme_poids_select']
            print("Somme poids achat", sum_poids_fixing)
            if poids_total_achat == sum_poids_fixing:
                try:
                    achat = Achat.objects.get(pk=serializer.data['achat']['id'])
                    print(achat)
                    achat.status = 3
                    date_time = timezone.now()
                    achat.updated_at = date_time
                    achat.updated_by = self.request.user
                    achat.save()
                except IndexError:
                    response = {"message": "Achat introuvable"}
                    return Response(response)

        # if type_envoie == 1:
        #     # Par barre
        #     fixing_detail_items = FixingDetail.objects.filter(achat=serializer.data['achat']['id'])
        #     # fixing_detail_items.values('achat_items')
        #     sum_poids_fixind_detail = 0
        #     for item in fixing_detail_items:
        #         poids = AchatItems.objects.get(pk=item.achat_items).poids_achat
        #         sum_poids_fixind_detail += poids
        #     if decimal.Decimal(sum_poids_fixind_detail) == decimal.Decimal(poids_total_achat):
        #         try:
        #             achat = Achat.objects.get(pk=serializer.data['achat']['id'])
        #             achat.status = 3
        #             achat.save()
        #         except IndexError:
        #             response = {"message": "Achat introuvable"}
        #             return Response(response)
        #     else:
        #         print("not equal to poids_ttal")
        # elif type_envoie == 2:
        #     # Envoie Global
        #     try:
        #         achat = Achat.objects.get(pk=serializer.data['achat']['id'])
        #         achat.status = 3
        #         achat.save()
        #     except IndexError:
        #         response = {"message": "Achat introuvable"}
        #         return Response(response)
        # elif type_envoie == 3:
        #     # Poids
        #     fixing_details = FixingDetail.objects.filter(type_envoie=3, achat=serializer.data['achat']['id'])
        #     sum_poids_fixing = fixing_details.aggregate(somme_poids_select=Sum('poids_select'))['somme_poids_select']
        #     print("poids total", sum_poids_fixing)
        #     if poids_total_achat == sum_poids_fixing:
        #         try:
        #             achat = Achat.objects.get(pk=serializer.data['achat']['id'])
        #             print(achat)
        #             achat.status = 3
        #             achat.save()
        #         except IndexError:
        #             response = {"message": "Achat introuvable"}
        #             return Response(response)

    @action(detail=True, methods=['GET'])
    def get_fixing_by_id(self, request, pk=None):
        # Le parametre pk contient la valeur transmise par url
        # ici il correspond a l'id du Fixing envoyé dans la requete

        if pk is not None:
            print("Id Fixing =", pk)
            # Recuperer le Fixing dont l'id a été reçu dans la requete
            errors = {}
            somme_poids_achat_items = 0.0
            # try:
            fixing = get_object_or_404(Fixing, pk=pk)
            # fixing = Fixing.objects.get(pk=pk)
            poids_fixe_dans_fixing = fixing.poids_fixe
            print("Poids fixe dans Fixing =", poids_fixe_dans_fixing)

            somme_poids_items = 0.00  # Recupere le poids de l'achat envoyé par items
            somme_poids_selected = 0.00  # Recupere le poids de l'achat envoyé par poids
            poids_total_achats = 0.00  # Recupere le poids de l'achat envoyé globalement
            # try:
            fixings_detail = FixingDetail.objects.filter(fixing=pk)
            # Faire la Somme des poids des achat envoyé par Poids
            somme_poids_select = fixings_detail.aggregate(somme_poids_select=Sum('poids_select'))['somme_poids_select']
            if somme_poids_select is not None:
                somme_poids_selected = somme_poids_select
            # except IndexError:
            #     errors["fixing_par_poids"] = "Pas de fixing par poids"
            #     response = {"fixing_detail": "Ce Fixing ne contient aucun Achat"}
            #     return Response(response)
            # try:
            # Recuperer le poids de l'Achat envoyé Globalement
            """" 
            Pour cela on recupere d'abord l'id de l'Achat dont
            La valeur de l'achat item correspondant est Null et la valeur du poids_select aussi est Null
            """
            if fixings_detail.values('achat_id').filter(achat_items=None, poids_select=None).exists():
                # Poids Total de l'achat depuis le model Achat
                id_achat = fixings_detail.values('achat_id').filter(achat_items=None, poids_select=None)
                if id_achat is not None:
                    achat_poids_total = id_achat.values('achat_id__poids_total')
                    poids_total_achat = achat_poids_total[0]['achat_id__poids_total']
                    if poids_total_achat is not None:
                        poids_total_achats = poids_total_achat
                        print("Poids Total de l'Achat envoyé par global", poids_total_achat)
            # except IndexError:
            #     errors["fixing_par_global"] = "Pas de fixing par envoie global"

            # try:
            # Tableau devant recevoir les IDs des Achat items se trouvant dans FixingDetail
            tab_id_achat_item = []
            if fixings_detail.values('achat_items').exists():
                id_achat_items = fixings_detail.values('achat_items')
                if id_achat_items is not None:
                    for id_achat_item in id_achat_items:
                        if id_achat_item['achat_items'] is not None:
                            print("Achat items dans fixing detail:", id_achat_item)
                            tab_id_achat_item.append(id_achat_item['achat_items'])
                        # else:
                        #     print("Achat items dans fixing detail est null")

                    """Faire la somme des poids des AchatItems envoyés par barre (Envoie Par Barre ou Items)"""
                    achat_items = AchatItems.objects.filter(id__in=tab_id_achat_item)
                    somme_poids_achat_items = achat_items.aggregate(
                        somme_poids_achat_item=Sum('poids_achat')
                    )['somme_poids_achat_item']
                    if somme_poids_achat_items is not None:
                        somme_poids_items = somme_poids_achat_items
            # except IndexError:
            #     errors["fixing_par_barres"] = "Pas de fixing envoyés par barre"

            """
                Faire la somme des poids calculé dans FixingDetail a travers l'ID du Fixing,
                Ensuite comparé au Poids fixé dans Fixing
            """

            poids_total_fixing_dans_fixing_detail = float(somme_poids_items) + float(somme_poids_selected) + float(
                poids_total_achats)

            print("\nPoids Total Calculé =", poids_total_fixing_dans_fixing_detail)
            if poids_total_fixing_dans_fixing_detail == poids_fixe_dans_fixing:
                reponse = {
                    "poids_total_fixing_dans_fixing_detail": poids_total_fixing_dans_fixing_detail,
                    "poids_fixe_dans_fixing": poids_fixe_dans_fixing,
                    "valeur_identique": True,
                }
                return Response(reponse)
            else:
                reponse = {
                    "poids_total_fixing_dans_fixing_detail": poids_total_fixing_dans_fixing_detail,
                    "poids_fixe_dans_fixing": poids_fixe_dans_fixing,
                    "valeur_identique": False,
                }
                return Response(reponse)
            # except IndexError:
            #     response = {"message": "Le Fixing d'id "+str(pk)+" est introuvable"}
            #     return Response(response, status=status.HTTP_404_NOT_FOUND)
            # except ValueError:
            #     response = {"message": "L'id doit etre de type entier"}
            #     return Response(response)
        else:
            response = {"message": "Veuillez fournir l'id du Fixing"}
            return Response(response, status=status.HTTP_204_NO_CONTENT)

    @action(detail=True, methods=['GET'])
    def fixing_valide(self, request, pk=None):
        #   A filtrer par Utilisateur, pk contient l'id de l'Utilisateur
        if pk is not None:
            try:
                fixing_valides = FixingDetail.objects.filter(created_by=pk).values(
                    'fournisseur__nom', 'fournisseur__prenom', 'fixing__poids_fixe', 'fixing__fixing_bourse', 'fournisseur',
                    'achat__poids_total', 'achat__carrat_moyen', 'fixing__discompte', 'created_at'
                ).annotate(
                    nb_valide=Count('ordre_validation'), achat_item=ArrayAgg('achat_items'),
                    poids_select=ArrayAgg('poids_select')
                ).order_by('-created_at')

                # Liste devant recevoir les dictionnaire des fixing detail regroupés par ordre de validation
                list_fixing_valides = []

                for fixing_valide in fixing_valides:
                    tab_items = fixing_valide['achat_item']
                    poids_select = fixing_valide['poids_select']
                    # if not fixing_valide['achat_item'].__contains__(None):

                    # Filtre la liste tab_items pour retirer toutes les valeurs None

                    val = None
                    my_tab_items = list(filter(lambda item: item != val, tab_items))

                    tab_poids_select = list(filter(lambda poids: poids != val, poids_select))

                    # Variable pour faire la somme des poids des AchatItems se trouvant dans FixingDetail
                    # utilisé pour la validation du Fixing
                    somme_poids_items = 0
                    # Tableau devant recevoir les infos de chaque AchatItems dans FixingDetail
                    tab_achat_items = []
                    for i in range(0, len(my_tab_items)):
                        print("tab_item de i", my_tab_items[i])
                        qs = AchatItems.objects.get(pk=my_tab_items[i])
                        somme_poids_items += qs.poids_achat
                        info_item = {
                            "poids": qs.poids_achat,
                            "carrat": qs.carrat_achat,
                            "manquant": qs.manquant,
                        }
                        # Ajouter chaque AchatItem ou barre dans le tableau suivit de la somme
                        # de leurs Poids
                        tab_achat_items.append(info_item)
                    tab_achat_items.append(somme_poids_items)
                    if not tab_poids_select:
                        # Dictionnaire de Fixing validé par Barre
                        fixing_valides_dict = {
                            "nom": fixing_valide['fournisseur__nom'],
                            "prenom": fixing_valide['fournisseur__prenom'],
                            "poids_fixe": fixing_valide['fixing__poids_fixe'],
                            "fixing_bourse": fixing_valide['fixing__fixing_bourse'],
                            "fournisseur": fixing_valide['fournisseur'],
                            "achat_poids_total": fixing_valide['achat__poids_total'],
                            "achat_carrat_moyen": fixing_valide['achat__carrat_moyen'],
                            "fixing_discompte": fixing_valide['fixing__discompte'],
                            "created_at": fixing_valide['created_at'],
                            "nb_valide": fixing_valide['nb_valide'],
                            "achat_item": tab_achat_items
                        }
                        list_fixing_valides.append(fixing_valides_dict)
                    elif not my_tab_items:
                        # Dictionnaire de Fixing validé par Poids
                        fixing_valides_dict = {
                            "nom": fixing_valide['fournisseur__nom'],
                            "prenom": fixing_valide['fournisseur__prenom'],
                            "poids_fixe": fixing_valide['fixing__poids_fixe'],
                            "fixing_bourse": fixing_valide['fixing__fixing_bourse'],
                            "fournisseur": fixing_valide['fournisseur'],
                            "achat_poids_total": fixing_valide['achat__poids_total'],
                            "achat_carrat_moyen": fixing_valide['achat__carrat_moyen'],
                            "fixing_discompte": fixing_valide['fixing__discompte'],
                            "created_at": fixing_valide['created_at'],
                            "nb_valide": fixing_valide['nb_valide'],
                            "poids_select": tab_poids_select
                        }
                        list_fixing_valides.append(fixing_valides_dict)
                    else:
                        # Dictionnaire de Fixing validé par Barre et par Poids
                        fixing_valides_dict = {
                            "nom": fixing_valide['fournisseur__nom'],
                            "prenom": fixing_valide['fournisseur__prenom'],
                            "poids_fixe": fixing_valide['fixing__poids_fixe'],
                            "fixing_bourse": fixing_valide['fixing__fixing_bourse'],
                            "fournisseur": fixing_valide['fournisseur'],
                            "achat_poids_total": fixing_valide['achat__poids_total'],
                            "achat_carrat_moyen": fixing_valide['achat__carrat_moyen'],
                            "fixing_discompte": fixing_valide['fixing__discompte'],
                            "created_at": fixing_valide['created_at'],
                            "nb_valide": fixing_valide['nb_valide'],
                            "achat_item": tab_achat_items
                        }
                        list_fixing_valides.append(fixing_valides_dict)
                        fixing_valides_dict = {
                            "nom": fixing_valide['fournisseur__nom'],
                            "prenom": fixing_valide['fournisseur__prenom'],
                            "poids_fixe": fixing_valide['fixing__poids_fixe'],
                            "fixing_bourse": fixing_valide['fixing__fixing_bourse'],
                            "fournisseur": fixing_valide['fournisseur'],
                            "achat_poids_total": fixing_valide['achat__poids_total'],
                            "achat_carrat_moyen": fixing_valide['achat__carrat_moyen'],
                            "fixing_discompte": fixing_valide['fixing__discompte'],
                            "created_at": fixing_valide['created_at'],
                            "nb_valide": fixing_valide['nb_valide'],
                            "poids_select": tab_poids_select
                        }
                        list_fixing_valides.append(fixing_valides_dict)

                return Response(list_fixing_valides, status.HTTP_200_OK)
            except IndexError:
                response = {"message": "Aucun fixing valide trouvé"}
                return Response(response, status=status.HTTP_404_NOT_FOUND)
            except ValueError:
                response = {"message": "L'id de l'utilisateur doit etre un nombre entier"}
                return Response(response, status.HTTP_400_BAD_REQUEST)
            except AssertionError:
                response = {"message": "L'id de l'utilisateur doit etre un nombre entier"}
                return Response(response, status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        fixing_details = get_list_or_404(FixingDetail)
        # grouper = FixingDetail.objects.all().annotate(fixing_count=Count('fixing_id'))
        return fixing_details


class FactureFournisseurViewSet(viewsets.ModelViewSet):
    queryset = FactureFournisseur.objects.all()
    serializer_class = FactureFournisseurSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class CaisseViewSet(viewsets.ModelViewSet):
    queryset = Caisse.objects.all()
    serializer_class = CaisseSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']

    def perform_create(self, serializer):
        user = self.request.user
        # serializer.save(created_by=user)
        serializer.save()

    @action(detail=True, methods=['GET'], name="Situation fournisseur")
    def situation_fournisseur(self, request, pk=None):
        if pk is not None:
            caisse_fournisseur = Caisse.objects.filter(fournisseur=pk)
            # print("Caisse fournisseur", caisse_fournisseur)
            caisse_fournisseur_ser = CaisseSerializer(caisse_fournisseur, many=True)
            # fixing_details = FixingDetail.objects.filter(fournisseur=pk)
            # fixing_details_ser = FixingDetailSerializer(fixing_details, many=True)
            # print(fixing_details)
            # response = {"caisse_fournisseur": caisse_fournisseur_ser.data, "fixing_detail": fixing_details_ser.data}

            id_achat_items = FixingDetail.objects.filter(fournisseur=pk).values('achat_items', 'fixing__fixing_bourse',
                                                                                'fixing__discompte'
                                                                                ).exclude(achat_items=None)
            tab_achat_items = []

            print("les id achat items", id_achat_items)
            for achat_item in id_achat_items:
                item = AchatItems.objects.get(pk=achat_item['achat_items'])
                prix_unit = (decimal.Decimal(achat_item['fixing__fixing_bourse']) / 34) - decimal.Decimal(achat_item['fixing__discompte'])
                achat_items = {"poids_item": item.poids_achat,
                               "carrat": item.carrat_achat, "manquant": item.manquant,
                               "fixing_bourse": achat_item['fixing__fixing_bourse'],
                               "discounte": achat_item['fixing__discompte'],
                               "prix_unit": prix_unit,
                               }
                tab_achat_items.append(achat_items)
            print("Les items", tab_achat_items)

            # Recuperer les poids
            poids_item = FixingDetail.objects.filter(fournisseur=pk).values('poids_select', 'achat__carrat_moyen',
                                                                            'fixing__fixing_bourse',
                                                                            'fixing__discompte',
                                                                            ).exclude(poids_select=None)

            for item in poids_item:
                prix_unit = item['fixing__fixing_bourse'] / 34 - item['fixing__discompte']
                fixing_item = {"poids_item": item['poids_select'],
                               "carrat": item['achat__carrat_moyen'], "manquant": 0,
                               "fixing_bourse": item['fixing__fixing_bourse'],
                               "discounte": item['fixing__discompte'],
                               "prix_unit": prix_unit,
                               }
                tab_achat_items.append(fixing_item)
            response = {"caisse_fournisseur": caisse_fournisseur_ser.data, "fixing_detail": tab_achat_items}
            return Response(response, status.HTTP_200_OK)
