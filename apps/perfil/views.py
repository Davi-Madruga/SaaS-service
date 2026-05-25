from rest_framework import viewsets, mixins
from .serializers import CadastroClienteSerializer, PerfilSerializer, CadastroUsuarioAdminSerializer
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from .models import Perfil
from apps.barbearia.permissions import IsAdmin

class CadastroClienteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CadastroClienteSerializer
    permission_classes = [AllowAny]

class PerfilViewSet(mixins.ListModelMixin,mixins.UpdateModelMixin,
mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        perfil = self.request.user.perfil

        if perfil.tipo == 'admin':
            return Perfil.objects.all()

        return Perfil.objects.filter(user=self.request.user)
    
class CadastroUsuarioAdminViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CadastroUsuarioAdminSerializer
    permission_classes = [IsAuthenticated,IsAdmin]
