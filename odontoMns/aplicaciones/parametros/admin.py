from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pais)
admin.site.register(Provincia)
admin.site.register(Localidad)
admin.site.register(Estado)
admin.site.register(Urgencia)