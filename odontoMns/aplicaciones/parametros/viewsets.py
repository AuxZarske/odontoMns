from rest_framework import viewsets
from .models import Pais, Estado, Urgencia, Provincia, Localidad
from .serializer import PaisSerializer, EstadoSerializer, UrgenciaSerializer, ProvinciaSerializer, LocalidadSerializer

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer 

class ProvinciaViewSet(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer 

class UrgenciaViewSet(viewsets.ModelViewSet):
    queryset = Urgencia.objects.all()
    serializer_class = UrgenciaSerializer 