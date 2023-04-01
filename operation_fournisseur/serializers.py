from rest_framework import serializers

from .models import *


class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = ('nom', 'prenom', 'adresse', 'telephone', 'email', 'pays', 'ville')


class AchatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achat
        fields = '__all__'


class CompteFournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteFournisseur
        fields = '__all__'


class OperationCompteFournisSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationCompteFournis
        fields = '__all__'


class LotArrivageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LotArrivage
        fields = '__all__'


class AttributionSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Attribution
        fields = '__all__'


class FixingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixing
        fields = '__all__'
