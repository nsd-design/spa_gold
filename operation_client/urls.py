from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from operation_client.views import *

router = routers.DefaultRouter()
router.register("client", ClientViewSet)
router.register("compt_client", CompteClientViewSet)
router.register("operation_compte_client", OperationCompteClientViewSet)
router.register("facture_expedition", FactureExpeditionViewSet)
router.register("expedition", ExpeditionViewSet)
router.register("vente", VenteViewSet)
router.register("vente/vente_detail", VenteViewSet)

urlpatterns = [
    path("", include(router.urls))
]
