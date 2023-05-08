from django.urls import path
from django.conf.urls import include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register("fournisseur", FournisseurViewSet)
router.register("achat", AchatViewSet)
router.register("achat_items", AchatItemsVieSet)
router.register("compte_fournisseur", CompteFournisseurViewSet)
router.register("operation_compte_fournisseur", OperationCompteFournisViewSet)
router.register("arrivage", LotArrivageViewSet)
router.register("attribution", AttributionViewSet)
router.register("fixing", FixingViewSet)
router.register("facture_fournisseur", FactureFournisseurViewSet)
router.register("fixing_detail", FixingDetailViewSet)
router.register("caisse", CaisseViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
