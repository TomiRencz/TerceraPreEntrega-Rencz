from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    precio = models.IntegerField()
    antiguedad = models.IntegerField()

class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email}"

class Comprador(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - E-Mail: {self.email}"

class Empresa(models.Model):
    nombre = models.CharField(max_length=30)
# Create your models here.
