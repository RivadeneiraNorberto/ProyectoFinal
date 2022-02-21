from cgitb import text
from distutils.command.upload import upload
from pyexpat import model
from tkinter.tix import InputOnly
from django.db import models
from django.db.models import Model,ForeignKey, CASCADE, ImageField
from django.contrib.auth.models import User


# Create your models here.
class Servicio(models.Model):
    nombre=models.CharField(max_length=50)
    descripcion=models.CharField(max_length=200)
    precio=models.FloatField()
    
    def __str__(self):
        return f'{self.nombre} - {self.descripcion} ($ {self.precio})'
    
class Tecnico(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}  {self.apellido} (Edad: {self.edad})'
    
class Insumo(models.Model):
    cantidad=models.IntegerField()
    nombre=models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.nombre}  (Cant.: {self.cantidad})'

class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares', null=True, blank=True)