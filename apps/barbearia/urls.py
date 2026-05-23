from rest_framework.routers import DefaultRouter
from .views import ServicoViewSet

router = DefaultRouter()

router.register(r'servicos', ServicoViewSet, basename='servico')

urlpatterns = router.urls