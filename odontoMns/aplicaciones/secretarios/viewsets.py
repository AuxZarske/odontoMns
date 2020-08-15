from rest_framework import viewsets
from .models import Secretario
from .serializer import SecretarioSerializer

class SecretarioViewSet(viewsets.ModelViewSet):
    queryset = Secretario.objects.all()
    serializer_class = SecretarioSerializer 