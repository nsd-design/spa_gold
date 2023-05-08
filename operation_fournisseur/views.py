import json
from datetime import datetime
from django.http import JsonResponse
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
    def create_f(self, request, pk=None):
        if 'telephone' in request.data:
            fournisseur = Fournisseur.objects.get(id=pk)
            user = Utilisateur.objects.get(id=1)
            print("User", user.username)
            print("Fournisseur ", fournisseur.nom, " ", fournisseur.prenom)

            response = {"message": "Succès"}
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {"message": "Numero de telephone manquant"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


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

    # def get(self):
    #     achat_by_user = Achat.objects.filter(created_by=self.request.user).order_by("-created_at").first()
    #     return achat_by_user

    def get_queryset(self):
        queryset = Achat.objects.all()

        # Recuperer les achats par Slug
        slug = self.request.query_params.get('slug')
        if slug:
            queryset = queryset.filter(slug=slug)
            return queryset

        """ Recuperer les achats d'apres une periode
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
                    qs = queryset.filter(created_at__gte=date_debut_to_local_date, created_at__lt=date_fin).select_related('fournisseur')
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


class AchatItemsVieSet(viewsets.ModelViewSet):
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
                print("Id fournisseur", id_fournisseur)
                achat_encours = Achat.objects.filter(fournisseur=id_fournisseur, status=1)
                print("Id achat en cours", achat_encours)
                id_achat = achat_encours[0].id
            except IndexError:
                msg = {"message": "Fournisseur introuvable"}
                return None

            try:

                achat_items = AchatItems.objects.filter(achat=id_achat, item_used=False)
                print("try achat items", achat_items)
                return achat_items
            except IndexError:
                print("Aucun item pour cet achat")
                msg = {"message": "Aucun item pour cet achat"}
                return None

            return achat_items

        return queryset.filter(item_used=False)

    # def perform_update(self, serializer):
    #
    #     datas = self.request.data
    #     print(datas)

    def partial_update(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        ids = request.data.get('id')
        objects = self.get
        return "OK"


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
