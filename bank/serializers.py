from rest_framework import serializers

from .models import *


class ParticulierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Particulier
        fields = '__all__'


class CompteParticulierSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteParticulier
        fields = '__all__'


class OperationParticulierSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationParticulier
        fields = '__all__'
