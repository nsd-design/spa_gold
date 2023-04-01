from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from .views import UtilisateurViewSet

router = routers.DefaultRouter()
router.register("user", UtilisateurViewSet)

urlpatterns = [
    path('', include(router.urls))
]
