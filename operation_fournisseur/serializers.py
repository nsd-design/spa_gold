from rest_framework import serializers

from .models import *


class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = ('id', 'nom', 'prenom', 'adresse', 'telephone', 'email', 'pays', 'ville')


class AchatSerializer(serializers.ModelSerializer):
    fournisseur = serializers.PrimaryKeyRelatedField(queryset=Fournisseur.objects.all())
    class Meta:
        model = Achat
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['fournisseur'] = FournisseurSerializer()
        return super(AchatSerializer, self).to_representation(instance)
    

class AchatItemsSerializer(serializers.ModelSerializer):
    achat = serializers.PrimaryKeyRelatedField(queryset=Achat.objects.all())
    
    def to_representation(self, instance):
        self.fields['achat'] = AchatSerializer()
        return super(AchatItemsSerializer, self).to_representation(instance)

    class Meta:
        model = AchatItems
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


class AttributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribution
        fields = '__all__'


class FixingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fixing
        fields = '__all__'
