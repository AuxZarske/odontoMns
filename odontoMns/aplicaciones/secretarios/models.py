from django.db import models
from odontoMns.aplicaciones.parametros.models import Localidad

# Create your models here.
class Secretario(models.Model):
    codSecre = models.AutoField(primary_key=True)
    apellido = models.CharField('Apellido del secretario', max_length = 60, null = False, blank = False)
    telefono = models.CharField('telefono', max_length = 20, null = False, blank = False)
    email = models.EmailField('Correo electronico', null =  False, blank = False)
    nombres = models.CharField('Nombrees', max_length = 60, null = False, blank = False)
    # direccion = models.CharField('Direccion de la empresa', max_length = 200, null = False, blank = False)
    area_geografica = models.ForeignKey(Localidad, on_delete = models.DO_NOTHING,  null = True, blank = True)