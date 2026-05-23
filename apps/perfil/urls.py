from rest_framework.routers import DefaultRouter
from .views import CadastroClienteViewSet

router = DefaultRouter()

router.register(r'clientes', CadastroClienteViewSet, basename='cliente')
urlpatterns = router.urls