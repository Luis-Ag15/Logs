from django.conf import settings
from django.db import models
from django.core.validators import RegexValidator
from .fields import EncryptedTextField, EncryptedDateField

# Validador alfanumérico (máx 10)
alphanumeric_10 = RegexValidator(
    regex=r'^[A-Za-z0-9]{1,10}$',
    message='El ID debe ser alfanumérico y tener máximo 10 caracteres.'
)

class Alumno(models.Model):

    # 🔑 LLAVE PRIMARIA AUTOINCREMENTAL
    codigo = models.BigAutoField(
        primary_key=True,
        verbose_name="Código interno"
    )

    # 🆔 ID ALFANUMÉRICO (QR)
    id = models.CharField(
        max_length=10,
        unique=True,
        validators=[alphanumeric_10],
        verbose_name="ID QR"
    )

    # 🔐 CAMPOS CIFRADOS
    nombre = EncryptedTextField(verbose_name="Nombre")
    fecha_nacimiento = EncryptedDateField(verbose_name="Fecha de nacimiento")
    email = EncryptedTextField(verbose_name="Correo electrónico")
    telefono = EncryptedTextField(verbose_name="Teléfono")
    fecha_de_registro = EncryptedDateField(verbose_name="Fecha de registro")
    texto = EncryptedTextField(verbose_name="Texto")

    # 📷 IMÁGENES (NO CIFRADAS)
    foto_perfil = models.ImageField(
        upload_to='images/perfil/',
        null=True,
        blank=True
    )

    foto_resultado = models.ImageField(
        upload_to='results/resultado/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.id} ({self.codigo})"

    class Meta:
        db_table = "alumnos"
        ordering = ["-codigo"]

class ScanLog(models.Model):
    scanner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='scan_logs',
        verbose_name="Escaneado por"
    )
    alumno = models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        related_name='scan_logs',
        verbose_name="Alumno Escaneado"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha y Hora"
    )

    class Meta:
        verbose_name = "Registro de Escaneo"
        verbose_name_plural = "Registros de Escaneos"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.scanner.username} escaneó a {self.alumno.id} el {self.timestamp}"
