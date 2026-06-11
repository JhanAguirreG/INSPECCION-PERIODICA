from django.contrib import admin
from .models import Institucion, Servicio, Equipo, InspeccionDiaria

admin.site.register(Institucion)
admin.site.register(Servicio)
admin.site.register(Equipo)
admin.site.register(InspeccionDiaria)
