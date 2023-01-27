from django.db import models

# Create your models here.

class Lote (models.Model):

    ESTATUS = (
        ('Ocupado','Ocupado'),
        ('Disponible','Disponible')
    )

    longitud = models.FloatField(null= True)
    ancho =  models.FloatField(null=True)
    precio = models.FloatField(null=True)
    estado = models.CharField(max_length=25, null = True,choices=ESTATUS)
    comprador = models.CharField(max_length=25,null=True, blank=True)
    vendedor = models.CharField(max_length=25, null=True, blank=True)
     
    def __str__ (self):
        return str(self.id)