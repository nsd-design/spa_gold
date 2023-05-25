import random

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=True, methods=['POST'])
    def create_expedition(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            serializer = ExpeditionSerializer(data=request.data, many=True)
            if serializer.is_valid():
                print("Expedition ser valide", serializer)
                code_exp = random.randint(1, 9999999999)
                for expedition in serializer.validated_data:

                    Expedition.objects.create(
                        lot_exp=expedition['lot_exp'], client_exp=expedition['client_exp'],
                        achat_items=expedition['achat_items'], type_envoie=expedition['type_envoie'],
                        code_exp=code_exp, status=expedition['status'],
                        created_by=expedition['created_by']
                    )
                    print("Expedition", expedition)
                response = {"message": "Enregistrement(s) effectués",}
                return Response(response, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            response = {"message": "User introuvable"}
            return Response(response, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['GET'])
    def liste_expeditions(self, request, pk=None):
        # Recuperer les expeditions (ventes) de l'utilisateur connecté
        try:
            expeditions = Expedition.objects.filter(created_by=pk).values(
                'lot_exp__designation', 'client_exp__raison_sociale', 'client_exp__responsable',
                'type_envoie', 'status', 'created_at'
            ).annotate(nb=Count('code_exp'), achat_items=ArrayAgg('achat_items'))
            # List devant recevoir le dictionnair customisé de chaque regroupement de l'expedition
            tab_expedition = []
            for expedition in expeditions:
                tab_achat_item = []
                # Recuperation des infos des achat items se trouvant dans l'expedition
                for id_item in expedition['achat_items']:
                    item = AchatItems.objects.get(pk=id_item)
                    current_item = {
                        "id": item.id,
                        "poids": item.poids_achat,
                        "carrat": item.carrat_achat,
                    }
                    # Ajouter les achat item d'une meme vente (expedition) dans le tableau 'tab_achat_item'
                    tab_achat_item.append(current_item)
                # Custom dictionnair
                current_expedition = {
                    "lot": expedition['lot_exp__designation'],
                    "raison_socile": expedition['client_exp__raison_sociale'],
                    "responsable": expedition['client_exp__responsable'],
                    "type_envoi": expedition['type_envoie'],
                    "created_at": expedition['created_at'],
                    "achat_items": tab_achat_item,
                }
                tab_expedition.append(current_expedition)

            response = {"data": tab_expedition}
            return Response(response, status.HTTP_200_OK)
        except IndexError:
            response = {"message": "Aucune Expedition enregistrée par cet Utilisateur"}
            return Response(response, status.HTTP_404_NOT_FOUND)


class VenteViewSet(viewsets.ModelViewSet):
    queryset = Vente.objects.all()
    serializer_class = VenteSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    # authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        user = self.request.user
        # serializer.save(created_by=user)
        serializer.save()


class VenteDetailViewSet(viewsets.ModelViewSet):
    queryset = VenteDetail.objects.all()
    serializer_class = VenteDetailSerializer
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']

    def perform_create(self, serializer):
        user = self.request.user
        # serializer.save(created_by=user)
        serializer.save()
