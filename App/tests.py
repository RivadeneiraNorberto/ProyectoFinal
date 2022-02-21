from django.test import TestCase

from App.views import TecnicoCreateView, Tecnicos
from App.models import Tecnico

# Create your tests here.
class TecnicoTestCase(TestCase):
    def test_alta_tecnico(self):
        tecnico = Tecnico(nombre = 'tecniconom', apellido = 'tecnicoape', edad = 30)
        tecnico.save()
        
        tecnicoEnBase = Tecnico.objects.get(id=tecnico.id)
        
        self.assertEquals(tecnicoEnBase.nombre, 'tecniconom')
        self.assertEquals(tecnicoEnBase.apellido, 'tecnicoape')
        self.assertEquals(tecnicoEnBase.edad, 30)