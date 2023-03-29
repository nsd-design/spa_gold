from django.shortcuts import render
from rest_framework import viewsets


from operation_client.serializers import *


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CompteClientViewSet(viewsets.ModelViewSet):
    queryset = CompteClient.objects.all()
    serializer_class = CompteClientSerializer


class OperationCompteClientViewSet(viewsets.ModelViewSet):
    queryset = OperationCompteClient.objects.all()
    serializer_class = OperationCompteClientSerializer


class FactureExpeditionViewSet(viewsets.ModelViewSet):
    queryset = FactureExpedition.objects.all()
    serializer_class = FactureExpeditionSerializer


class ExpeditionViewSet(viewsets.ModelViewSet):
    queryset = Expedition.objects.all()
    serializer_class = ExpeditionSerializer


class VenteViewSet(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer
