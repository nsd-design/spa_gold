from django.http import HttpResponse

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from utilisateurs.models import Utilisateur
from .serializers import *
from django.core import serializers


class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

    def perform_create(self, serializer):
        """Create new Fournisseur"""
        serializer.save(created_by=self.request.user)


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


class CompteFournisseurViewSet(viewsets.ModelViewSet):
    queryset = CompteFournisseur.objects.all()
    serializer_class = CompteFournisseurSerializer


class OperationCompteFournisViewSet(viewsets.ModelViewSet):
    queryset = OperationCompteFournis.objects.all()
    serializer_class = OperationCompteFournisSerializer


class LotArrivageViewSet(viewsets.ModelViewSet):
    queryset = LotArrivage.objects.all()
    serializer_class = LotArrivageSerializer


class AttributionViewSet(viewsets.ModelViewSet):
    queryset = Attribution.objects.filter()
    serializer_class = AttributionSerializer


class FixingViewSet(viewsets.ModelViewSet):
    queryset = Fixing.objects.all()
    serializer_class = FixingSerializer

