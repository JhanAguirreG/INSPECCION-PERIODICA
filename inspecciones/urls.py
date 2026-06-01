

#urlpatterns = [
 #   path('', views.seleccionar_servicio, name='seleccionar'),
  #  path('seleccionar/', views.seleccionar_servicio, name='seleccionar'),
   # path('cargar-servicios/', views.cargar_servicios, name='cargar_servicios'),
    #path('nueva/', views.nueva_inspeccion, name='nueva_inspeccion'),

#]

from django.urls import path
from . import views

urlpatterns = [

    # Dashboard después de login
    path('dashboard/', views.dashboard, name='dashboard'),

    # Selector inicial
    path('', views.seleccionar_servicio, name='seleccionar'),
    path('seleccionar/', views.seleccionar_servicio, name='seleccionar'),

    # AJAX cargar servicios
    path('cargar-servicios/', views.cargar_servicios, name='cargar_servicios'),

    # Nueva inspección
    path('nueva/', views.nueva_inspeccion, name='nueva_inspeccion'),

]