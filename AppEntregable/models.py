from django.db import models

# Create your models here.
class Papa(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad= models.IntegerField()

class Mama(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad= models.IntegerField()
    profesion=models.CharField(max_length=50)

class Hermano(models.Model):
    nombre=models.CharField(max_length=50)
    fecha_de_llegada=models.DateField()
    edad=models.IntegerField()