from django.db import models

# Create your models here.
class Pais(models.Model):
    codPais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length = 60)

class Provincia(models.Model):
    codProv = models.AutoField(primary_key=True)
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE, null = False, blank = False)
    nombre_prov = models.CharField(max_length = 80)

class Localidad(models.Model):
    codLoc = models.AutoField(primary_key=True)
    provincia = models.ForeignKey(Provincia, on_delete = models.CASCADE, null = False, blank = False)
    nombre_loc = models.CharField(max_length = 80)
    cod_post = models.IntegerField(null = True, blank = True)

class Estado(models.Model):
    codEst = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length = 60)

class Urgencia(models.Model):
    codUrg = models.AutoField(primary_key=True)
    nombre_urgencia = models.CharField(max_length = 60)