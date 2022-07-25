from django.db import models

# Create your models here.
class Producto(models.Model):
    name_of_product = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    details = models.TextField()
# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Nombre: {self.name_of_product } - Precio {self.price} - Detalle {self.details} "

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
# con esta indicación comenzamos a ver detalladamente en nuestra BD
    def __str__(self):
        return f"Nombre: {self.nombre } - Apellido {self.apellido} - Edad {self.edad} "
    
class Vencimiento(models.Model):
    nombre= models.CharField(max_length=30)
    fecha_vencimiento= models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre } - Fecha de Vencimiento {self.fecha_vencimiento} "