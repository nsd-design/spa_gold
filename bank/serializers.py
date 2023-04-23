from rest_framework import serializers

from utilisateurs.serializers import UtilisateurSerializer
from .models import *


class ParticulierSerializer(serializers.ModelSerializer):
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)
    updated_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)

    def to_representation(self, instance):
        self.fields['created_by'] = UtilisateurSerializer()
        self.fields['updated_by'] = UtilisateurSerializer()
        return super(ParticulierSerializer, self).to_representation(instance)

    class Meta:
        model = Particulier
        fields = '__all__'


class CompteParticulierSerializer(serializers.ModelSerializer):
    particulier = serializers.PrimaryKeyRelatedField(queryset=Particulier.objects.all(), required=False)
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)

    def to_representation(self, instance):
        self.fields['particulier'] = ParticulierSerializer()
        self.fields['created_by'] = UtilisateurSerializer()
        return super(CompteParticulierSerializer, self).to_representation(instance)

    class Meta:
        model = CompteParticulier
        fields = '__all__'


class OperationParticulierSerializer(serializers.ModelSerializer):
    compte_particulier = serializers.PrimaryKeyRelatedField(queryset=CompteParticulier.objects.all(), required=False)
    created_by = serializers.PrimaryKeyRelatedField(queryset=Utilisateur.objects.all(), required=False)

    def to_representation(self, instance):
        self.fields['compte_particulier'] = CompteParticulierSerializer()
        self.fields['created_by'] = UtilisateurSerializer()
        return super(OperationParticulierSerializer, self).to_representation(instance)

    class Meta:
        model = OperationParticulier
        fields = '__all__'
