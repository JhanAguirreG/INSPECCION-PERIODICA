from django.db import models
from django.contrib.auth.models import User
import os


class Institucion(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class InspeccionDiaria(models.Model):

    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

    consecutivo = models.IntegerField()
    fecha = models.DateField(auto_now_add=True)

    observaciones = models.TextField(blank=True)

    # Firmas como imágenes reales
    firma_jefe = models.ImageField(upload_to='firmas/', blank=True, null=True)
    firma_verificacion = models.ImageField(upload_to='firmas/', blank=True, null=True)

    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)

    bloqueado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.servicio} - {self.consecutivo}"

class PerfilUsuario(models.Model):

    ROLES = (
        ('SUPERADMIN', 'Super Administrador'),
        ('ADMIN_CLINICA', 'Administrador Clínica'),
        ('BIOMEDICO', 'Biomédico'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institucion = models.ForeignKey(
        'Institucion',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    rol = models.CharField(
        max_length=20,
        choices=ROLES,
        default='BIOMEDICO'
        )

    def __str__(self):
        return f"{self.user.username} - {self.rol}"

class Equipo(models.Model):
    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        related_name="equipos"
    )
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.nombre} ({self.servicio.nombre})"
