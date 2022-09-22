from unicodedata import name
from django.db import models

# Create your models here.

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        cadena=self.nombre+"-"+self.descripcion
        return cadena



