from rest_framework import serializers

from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class CompteClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteClient
        fields = '__all__'


class OperationCompteClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationCompteClient
        fields = '__all__'


class FactureExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactureExpedition
        fields = '__all__'


class ExpeditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expedition
        fields = '__all__'


class VenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vente
        fields = '__all__'



