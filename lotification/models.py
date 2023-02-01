from django.db import models

# Create your models here.

# class time_struct(models.Model):
#     nombre = models.CharField(max_length=50)
#     lastupdated = models.DateTimeField(auto_now=True)
#     added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.nombre)

class Compradores(models.Model):
    nombre = models.CharField(max_length=25)
    numero = models.BigIntegerField()

    def __str__(self):
        return str(self.nombre)

class Espacios(models.Model):
    area = models.FloatField()
    precio = models.FloatField()
    comprador = models.ForeignKey(Compradores, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)
class Clients(models.Model):
    client_name = models.CharField(max_length=20, null=True)
    client_last_name = models.CharField(max_length=20,null=True)
    client_phone =models.BigIntegerField(null=True)
    client_direction = models.TextField(null=True)
    def __str__(self):
        return str(self.client_name)
class Pots(models.Model):
    options = (
    ("Disponible","Disponible"),
    ("Ocupado","Ocupado")
    )
    pot_large = models.FloatField()
    pot_width = models.FloatField()
    pot_price = models.FloatField()
    pot_dispo = models.CharField(max_length=20,choices=options, default="Disponible")
    pot_owner = models.ForeignKey(Clients, null=True,blank=True, on_delete=models.CASCADE)

class Payments(models.Model):
    Payment_amount = models.FloatField()
    Payment_date = models.DateField(auto_now_add=True)
    Payment_Pot = models.ForeignKey(Pots,null=True,on_delete=models.CASCADE)