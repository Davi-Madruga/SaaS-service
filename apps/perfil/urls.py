from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CadastroClienteViewSet, PerfilViewSet, CadastroUsuarioAdminViewSet, BarbeiroViewSet
from django.urls import path,include

router = DefaultRouter()

router.register(r'usuarios', CadastroUsuarioAdminViewSet, basename="usuario")
router.register(r'clientes', CadastroClienteViewSet, basename='cliente')
router.register(r'perfis', PerfilViewSet, basename='perfil')
router.register(r'barbeiros', BarbeiroViewSet, basename='barbeiro')

urlpatterns = [
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
