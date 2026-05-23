from rest_framework import viewsets, mixins
from .serializers import CadastroClienteSerializer
from rest_framework.permissions import AllowAny


class CadastroClienteViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CadastroClienteSerializer
    permission_classes = [AllowAny]
