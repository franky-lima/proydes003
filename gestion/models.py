from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, int_list_validator

# Create your models here.


class Entidad(models.Model):
	razonSocial = models.CharField(max_length=100)
	ruc = models.CharField(help_text="RUC PERÚ", max_length=11, validators=[int_list_validator(sep=''),MinLengthValidator(11),])
	direccionFiscal =models.CharField(max_length=100)
	contacto = models.CharField(max_length=100)
	telefono = models.CharField(help_text="051123456789", max_length=12, validators=[int_list_validator(sep=''),MinLengthValidator(12),])
	correo = models.EmailField(max_length=254, help_text='correo@dominio.com', unique=True)
	cuenta = models.CharField(max_length=42)

def __str__(self):
        return self.razonSocial

def registro(self):
	return self.fechaRegistro

def cuenta(self):
	return self.cuenta