from django.db import models
from odontoMns.aplicaciones.parametros.models import Localidad

# Create your models here.
class Proveedor(models.Model):
    codProve = models.AutoField(primary_key=True)
    empresa = models.CharField('Nombre de la empresa', max_length = 100, null = False, blank = False)
    telefono = models.CharField('telefono', max_length = 20, null = False, blank = False)
    email = models.EmailField('Correo electronico', null =  False, blank = False)
    contacto = models.CharField('Nombre del contacto', max_length = 60, null = False, blank = False)
    nota_general = models.TextField('nota descriptiva del proveedor', null = False, blank = False)
    direccion = models.CharField('Direccion de la empresa', max_length = 200, null = False, blank = False)
    area_geografica = models.ForeignKey(Localidad, on_delete = models.DO_NOTHING,  null = True, blank = True)