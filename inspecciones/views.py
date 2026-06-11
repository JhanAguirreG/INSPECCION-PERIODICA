from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Equipo, InspeccionDiaria


@login_required
def dashboard(request):

    equipos_operativos = Equipo.objects.filter(estado="OPERATIVO").count()
    equipos_falla = Equipo.objects.filter(estado="FALLA").count()
    inspecciones_pendientes = InspeccionDiaria.objects.filter(estado="PENDIENTE").count()

    return render(request, "dashboard.html", {
        "equipos_operativos": equipos_operativos,
        "equipos_falla": equipos_falla,
        "inspecciones_pendientes": inspecciones_pendientes,
    })