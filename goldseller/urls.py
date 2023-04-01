from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('operation_fournisseur.urls')),
    path('client_api/', include('operation_client.urls')),
    path('particulier_api/', include('bank.urls')),
    path('api/', include('utilisateurs.urls'))
]
