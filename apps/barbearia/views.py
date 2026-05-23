from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .serializers import ServicoSerializer
from .permissions import IsAdmin
from .models import Servico

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return[IsAuthenticated()]
        return[IsAuthenticated(),IsAdmin()]
