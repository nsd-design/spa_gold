from django.contrib import admin

from .models import *

admin.site.register(Particulier)
admin.site.register(CompteParticulier)
admin.site.register(OperationParticulier)
