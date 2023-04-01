from rest_framework import serializers

from .models import Utilisateur


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = Utilisateur.objects.create_user(**validated_data)
        return user
