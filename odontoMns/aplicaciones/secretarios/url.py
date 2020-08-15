from rest_framework import routers

from .viewsets import SecretarioViewSet

router = routers.SimpleRouter()
router.register('secretarios', SecretarioViewSet)


urlpatterns = router.urls