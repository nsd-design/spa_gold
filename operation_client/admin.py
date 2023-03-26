from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(CompteClient)
admin.site.register(OperationCompteClient)
admin.site.register(FactureExpedition)
admin.site.register(Expedition)
admin.site.register(Vente)
