from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):

    ROLES = [
        ('SUPERADMIN', 'Superadmin'),
        ('ADMIN_CLINICA', 'Admin Clínica'),
        ('BIOMEDICO', 'Biomédico'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    rol = models.CharField(max_length=20, choices=ROLES)

    institucion = models.ForeignKey(
        'Institucion',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username
# --------------------------------------------------
# INSTITUCIÓN
# --------------------------------------------------
class Institucion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


# --------------------------------------------------
# SERVICIO
# --------------------------------------------------
class Servicio(models.Model):
    nombre = models.CharField(max_length=200)

    institucion = models.ForeignKey(
        Institucion,
        on_delete=models.CASCADE,
        related_name="servicios"
    )

    def __str__(self):
        return self.nombre


# --------------------------------------------------
# EQUIPO
# --------------------------------------------------
class Equipo(models.Model):
    nombre = models.CharField(max_length=200)

    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        related_name="equipos"
    )

    estado = models.CharField(
        max_length=20,
        choices=[
            ('OPERATIVO', 'Operativo'),
            ('FALLA', 'Falla'),
        ],
        default='OPERATIVO'
    )

    def __str__(self):
        return self.nombre


# --------------------------------------------------
# INSPECCIÓN
# --------------------------------------------------
class InspeccionDiaria(models.Model):

    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    consecutivo = models.IntegerField(default=1)

    estado = models.CharField(
        max_length=20,
        choices=[
            ('PENDIENTE', 'Pendiente'),
            ('APROBADA', 'Aprobada'),
            ('RECHAZADA', 'Rechazada'),
        ],
        default='PENDIENTE'
    )

    observaciones = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Inspección {self.id}"

