from cgitb import text
from tkinter.tix import InputOnly
from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    precio=models.FloatField()
    
class Tecnico(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    
class Insumo(models.Model):
    cantidad=models.IntegerField()
    nombre=models.CharField(max_length=50)
    
