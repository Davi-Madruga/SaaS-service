from rest_framework import viewsets
from .models import Servico
from .serializers import ServicoSerializer
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .permissions import IsAdmin

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return[IsAuthenticated()]
        return[IsAuthenticated(),IsAdmin()]