from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from .serializers import ServicoSerializer, AgendamentoSerializer
from .permissions import IsAdmin
from .models import Servico, Agendamento
from rest_framework.exceptions import PermissionDenied

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return[IsAuthenticated()]
        return[IsAuthenticated(),IsAdmin()]

class AgendamentoViewSet(viewsets.ModelViewSet):
    serializer_class = AgendamentoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Agendamento.objects.all().select_related(
                "cliente",
                "barbeiro"
            ).prefetch_related("servicos")

        perfil = user.perfil

        if perfil.tipo == "admin":
            return Agendamento.objects.all().select_related(
                "cliente",
                "barbeiro"
            ).prefetch_related("servicos")

        if perfil.tipo == "barbeiro":
            return Agendamento.objects.filter(
                barbeiro=perfil
            ).select_related(
                "cliente",
                "barbeiro"
            ).prefetch_related("servicos")

        return Agendamento.objects.filter(
            cliente=perfil
        ).select_related(
            "cliente",
            "barbeiro"
        ).prefetch_related("servicos")

    def perform_create(self, serializer):
        perfil = self.request.user.perfil

        if perfil.tipo != "cliente":
            raise PermissionDenied(
                "Apenas clientes podem criar agendamentos."
            )

        serializer.save(cliente=perfil)