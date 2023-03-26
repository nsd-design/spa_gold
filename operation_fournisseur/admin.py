from django.contrib import admin

from .models import *

admin.site.register(Fournisseur)
admin.site.register(Achat)
admin.site.register(CompteFournisseur)
admin.site.register(OperationCompteFournis)
admin.site.register(LotArrivage)
admin.site.register(Attribution)
admin.site.register(Fixing)
