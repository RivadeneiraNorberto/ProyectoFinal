from django.forms import CharField, FloatField, Form, IntegerField

class formAltaServicio(Form):
    nombre=CharField()
    descripcion=CharField()
    precio=FloatField()
    
class formAltaTecnico(Form):
    nombre=CharField()
    apellido=CharField()
    edad=IntegerField()
            
class formAltaInsumo(Form):
    cantidad=IntegerField()
    nombre=CharField()
    
