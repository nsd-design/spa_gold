from django.shortcuts import render
from rest_framework import viewsets


from operation_client.serializers import *


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class CompteClientViewSet(viewsets.ModelViewSet):
    queryset = CompteClient.objects.all()
    serializer_class = CompteClientSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class OperationCompteClientViewSet(viewsets.ModelViewSet):
    queryset = OperationCompteClient.objects.all()
    serializer_class = OperationCompteClientSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class FactureExpeditionViewSet(viewsets.ModelViewSet):
    queryset = FactureExpedition.objects.all()
    serializer_class = FactureExpeditionSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class ExpeditionViewSet(viewsets.ModelViewSet):
    queryset = Expedition.objects.all()
    serializer_class = ExpeditionSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class VenteViewSet(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
