from rest_framework import routers

from .viewsets import PaisViewSet, EstadoViewSet, UrgenciaViewSet, ProvinciaViewSet, LocalidadViewSet

router = routers.SimpleRouter()
router.register('paises', PaisViewSet)
router.register('provincias', ProvinciaViewSet)
router.register('localidades', LocalidadViewSet)
router.register('estados', EstadoViewSet)
router.register('urgencias', UrgenciaViewSet)

urlpatterns = router.urls