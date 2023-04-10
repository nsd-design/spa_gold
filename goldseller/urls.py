from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('operation_fournisseur.urls')),
    path('client_api/', include('operation_client.urls')),
    path('particulier_api/', include('bank.urls')),
    path('api/', include('utilisateurs.urls')),
    path('auth/', obtain_auth_token),
]
