from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Institucion, Servicio, Equipo, InspeccionDiaria, PerfilUsuario

admin.site.register(Institucion)
admin.site.register(Servicio)
admin.site.register(Equipo)
admin.site.register(InspeccionDiaria)
admin.site.register(PerfilUsuario)
