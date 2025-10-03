from django.db import models


class Usuario(models.Model):
    ROLES = [
        ('admin', 'Administrador'),
        ('gestor', 'Gestor'),
    ]
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    rol = models.CharField(max_length=20, choices=ROLES)

    def __str__(self):
        return self.nombre


class Empresa(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
    identificador = models.CharField(
        max_length=20, unique=True)  # RUT o similar

    def __str__(self):
        return f"{self.nombre} ({self.pais})"


class Instrumento(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class CalificacionTributaria(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    año = models.IntegerField()
    nota = models.CharField(max_length=10)
    comentario = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.empresa} - {self.año}: {self.nota}"
