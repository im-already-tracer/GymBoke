from django.db import models
from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone

# Create your models here.

class Usuario(models.Model):
    dni = models.CharField(max_length=255, primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    ultimoIngreso = models.DateTimeField(auto_now_add=True, null= True)
    ultimoPago = models.DateTimeField(auto_now_add=True, null= True)
    venceCuota = models.DateTimeField(null=True)


    def asignar_fecha_vencimiento_cuota(self):
        # Obtener la fecha actual
        fecha_actual = datetime.now()

        # Agregar un mes a la fecha actual
        nueva_fecha = fecha_actual + relativedelta(months=1)  # Aproximadamente un mes

        # Asignar la nueva fecha al campo venceCuota
        self.venceCuota = nueva_fecha
        self.save()

def __str__(self):
    return (f'Usuario: {self.dni}: Nombre: {self.nombre}, Apellido :{self.apellido}, UltimoIngreso : {self.ultimoIngreso},  '
            f'ultimoPago : {self.ultimoPago}, venceCuota : {self.venceCuota}')