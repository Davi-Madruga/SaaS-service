from rest_framework import viewsets, mixins
from .serializers import RegistroSerializer
from rest_framework.permissions import AllowAny


class RegistroViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = RegistroSerializer
    permission_classes = [AllowAny]