import os
import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image as RLImage
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

from .models import Institucion, Servicio, Equipo, InspeccionDiaria


# ==========================================================
# DASHBOARD SEGÚN ROL
# ==========================================================

@login_required
def dashboard(request):

    perfil = request.user.perfilusuario

    if perfil.rol == 'SUPERADMIN':
        return render(request, 'dashboard_superadmin.html')

    elif perfil.rol == 'ADMIN_CLINICA':
        return render(request, 'dashboard_admin.html')

    elif perfil.rol == 'BIOMEDICO':
        return render(request, 'dashboard_biomedico.html')

    return redirect('login')


# ==========================================================
# SELECCIONAR INSTITUCIÓN Y SERVICIO
# ==========================================================

@login_required
def seleccionar_servicio(request):

    perfil = request.user.perfilusuario

    # SUPERADMIN puede ver todas
    if perfil.rol == 'SUPERADMIN':
        instituciones = Institucion.objects.all()
    else:
        instituciones = Institucion.objects.filter(
            id=perfil.institucion.id
        )

    if request.method == "POST":
        institucion_id = request.POST.get("institucion")
        servicio_id = request.POST.get("servicio")

        return redirect(
            f"/inspecciones/nueva/?institucion={institucion_id}&servicio={servicio_id}"
        )

    return render(request, "inspecciones/seleccionar.html", {
        "instituciones": instituciones
    })


# ==========================================================
# AJAX CARGAR SERVICIOS
# ==========================================================

@login_required
def cargar_servicios(request):

    institucion_id = request.GET.get("institucion_id")

    servicios = Servicio.objects.filter(
        institucion_id=institucion_id
    )

    data = [
        {"id": s.id, "nombre": s.nombre}
        for s in servicios
    ]

    return JsonResponse(data, safe=False)


# ==========================================================
# NUEVA INSPECCIÓN
# ==========================================================

@login_required
def nueva_inspeccion(request):

    institucion_id = request.GET.get("institucion")
    servicio_id = request.GET.get("servicio")

    institucion = get_object_or_404(
        Institucion,
        id=institucion_id
    )

    servicio = get_object_or_404(
        Servicio,
        id=servicio_id,
        institucion=institucion
    )

    equipos = servicio.equipos.all()

    if request.method == "POST":

        # -----------------------------------------
        # CONSECUTIVO AUTOMÁTICO POR SERVICIO
        # -----------------------------------------

        ultimo = InspeccionDiaria.objects.filter(
            servicio=servicio
        ).order_by('-consecutivo').first()

        if ultimo:
            nuevo_consecutivo = ultimo.consecutivo + 1
        else:
            nuevo_consecutivo = 1

        inspeccion = InspeccionDiaria.objects.create(
            institucion=institucion,
            servicio=servicio,
            consecutivo=nuevo_consecutivo,
            observaciones=request.POST.get("observaciones")
        )

        # -----------------------------------------
        # GUARDAR FIRMAS
        # -----------------------------------------

        def guardar_firma(base64_string, nombre):
            if base64_string:
                format, imgstr = base64_string.split(';base64,')
                ext = format.split('/')[-1]
                file_name = f"{nombre}_{inspeccion.id}.{ext}"
                file = ContentFile(base64.b64decode(imgstr), name=file_name)
                return file
            return None

        firma_jefe = guardar_firma(
            request.POST.get("firma_jefe"),
            "firma_jefe"
        )

        firma_verificacion = guardar_firma(
            request.POST.get("firma_verificacion"),
            "firma_verificacion"
        )

        if firma_jefe:
            inspeccion.firma_jefe.save(firma_jefe.name, firma_jefe)

        if firma_verificacion:
            inspeccion.firma_verificacion.save(
                firma_verificacion.name,
                firma_verificacion
            )

        # -----------------------------------------
        # GENERAR PDF
        # -----------------------------------------

        pdf_path = os.path.join(
            settings.MEDIA_ROOT,
            f"pdfs/inspeccion_{inspeccion.id}.pdf"
        )

        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

        doc = SimpleDocTemplate(pdf_path, pagesize=A4)
        elements = []
        styles = getSampleStyleSheet()

        elements.append(
            Paragraph(
                "<b>INSPECCIÓN PERIÓDICA EQUIPOS BIOMÉDICOS</b>",
                styles["Title"]
            )
        )
        elements.append(Spacer(1, 12))

        tabla_data = [["EQUIPO", "OBSERVACIÓN"]]

        for equipo in equipos:
            obs = request.POST.get(f"observacion_{equipo.id}", "")
            tabla_data.append([equipo.nombre, obs])

        tabla = Table(tabla_data, colWidths=[250, 250])

        tabla.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f37021")),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(tabla)
        doc.build(elements)

        inspeccion.pdf = f"pdfs/inspeccion_{inspeccion.id}.pdf"
        inspeccion.save()

        return redirect('dashboard')

    return render(request, "inspecciones/nueva.html", {
        "servicio": servicio,
        "equipos": equipos
    })