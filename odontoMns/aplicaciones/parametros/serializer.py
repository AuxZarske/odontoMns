from .models import Pais, Estado, Urgencia, Provincia, Localidad
from rest_framework import serializers


class PaisSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Pais
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Provincia
        fields = '__all__'

class LocalidadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Localidad
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Estado
        fields = '__all__'

class UrgenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Urgencia
        fields = '__all__'