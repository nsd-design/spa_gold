from rest_framework import serializers

from operation_fournisseur.serializers import FournisseurSerializer, AchatSerializer, AchatItemsSerializer, LotArrivageSerializer
from utilisateurs.serializers import UtilisateurSerializer
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)

    class Meta:
        model = Client
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['created_by'] = UtilisateurSerializer()
        return super(ClientSerializer, self).to_representation(instance)


class CompteClientSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False)
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)

    def to_representation(self, instance):
        self.fields['client'] = ClientSerializer()
        self.fields['created_by'] = UtilisateurSerializer()
        return super(CompteClientSerializer, self).to_representation(instance)

    class Meta:
        model = CompteClient
        fields = '__all__'


class OperationCompteClientSerializer(serializers.ModelSerializer):
    compte_client = serializers.PrimaryKeyRelatedField(queryset=CompteClient.objects.all(), required=False)
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)

    def to_representation(self, instance):
        self.fields['compte_client'] = CompteClientSerializer()
        self.fields['created_by'] = UtilisateurSerializer()
        return super(OperationCompteClientSerializer, self).to_representation(instance)

    class Meta:
        model = OperationCompteClient
        fields = '__all__'


class FactureExpeditionSerializer(serializers.ModelSerializer):
    fournisseur_exp = serializers.PrimaryKeyRelatedField(queryset=FactureExpedition.objects.all(), required=False)
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)

    def to_representation(self, instance):
        self.fields['fournisseur_exp'] = FournisseurSerializer()
        self.fields['created_by'] = UtilisateurSerializer()
        return super(FactureExpeditionSerializer, self).to_representation(instance)

    class Meta:
        model = FactureExpedition
        fields = '__all__'


class ExpeditionSerializer(serializers.ModelSerializer):
    client_exp = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False)
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)
    
    def to_representation(self, instance):
        self.fields['client_exp'] = ClientSerializer()
        self.fields['created_by'] = UtilisateurSerializer()
        return super(ExpeditionSerializer, self).to_representation(instance)
    
    class Meta:
        model = Expedition
        fields = '__all__'


class VenteSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=False)
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)

    def to_representation(self, instance):
        self.fields['client'] = ClientSerializer()
        self.fields['created_by'] = UtilisateurSerializer()
        return super(VenteSerializer, self).to_representation(instance)

    class Meta:
        model = Vente
        fields = '__all__'


class VenteDetailSerializer(serializers.ModelSerializer):
    vente = serializers.PrimaryKeyRelatedField(queryset=Vente.objects.all(), required=False)
    achat_item = serializers.PrimaryKeyRelatedField(queryset=AchatItems.objects.all(), required=False)

    def to_representation(self, instance):
        self.fields['vente'] = VenteSerializer()
        self.fields['achat_item'] = AchatItemsSerializer()
        return super(VenteDetailSerializer, self).to_representation(instance)

    class Meta:
        model = VenteDetail
        fields = '__all__'
