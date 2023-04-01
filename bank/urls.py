from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register("particulier", ParticulierViewSet)
router.register("compte_particulier", CompteParticulierViewSet)
router.register("operation_particulier", OperationParticulierViewSet)

urlpatterns = [
    path('', include(router.urls))
]
