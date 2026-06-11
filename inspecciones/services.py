from .models import InspeccionDiaria

def generar_consecutivo(servicio):
    ultimo = InspeccionDiaria.objects.filter(servicio=servicio).order_by('-consecutivo').first()
    return (ultimo.consecutivo + 1) if ultimo else 1