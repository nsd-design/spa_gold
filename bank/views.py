from rest_framework import viewsets

from .serializers import *


class ParticulierViewSet(viewsets.ModelViewSet):
    queryset = Particulier.objects.all()
    serializer_class = ParticulierSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class CompteParticulierViewSet(viewsets.ModelViewSet):
    queryset = CompteParticulier.objects.all()
    serializer_class = CompteParticulierSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']


class OperationParticulierViewSet(viewsets.ModelViewSet):
    queryset = OperationParticulier.objects.all()
    serializer_class = OperationParticulierSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
