from rest_framework.permissions import BasePermission
from django.core.exceptions import ObjectDoesNotExist

class IsAdmin(BasePermission):
    message = 'Apenas administradores podem gerenciar serviços.'

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        try:
            return request.user.perfil.tipo == 'admin'
        except ObjectDoesNotExist:
            return False