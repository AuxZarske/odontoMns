from .models import Secretario
from rest_framework import serializers


class SecretarioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Secretario
        fields = '__all__'