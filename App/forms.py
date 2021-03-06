from wsgiref.validate import validator
from django.forms import Form, CharField, FloatField, ImageField, IntegerField
from django.core.validators import RegexValidator

class formAltaServicio(Form):
    nombre= CharField(max_length=50, validators=[RegexValidator(regex='^[a-zA-Z]*$', message="Sólo se permiten letras.")])
    descripcion=CharField()
    precio=FloatField()
#Se deja de usar por ListView    
class formAltaTecnico(Form):
    nombre= CharField(max_length=50, validators=[RegexValidator(regex='^[a-zA-Z]*$', message="Sólo se permiten letras.")])
    apellido= CharField(max_length=50, validators=[RegexValidator(regex='^[a-zA-Z]*$', message="Sólo se permiten letras.")])
    edad=IntegerField()
            
class formAltaInsumo(Form):
    cantidad=IntegerField()
    nombre=CharField()
    
class FormAvatar(Form):
    imagen = ImageField(required=True)