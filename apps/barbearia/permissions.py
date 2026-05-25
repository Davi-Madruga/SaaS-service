from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = "Apenas administradores podem acessar este recurso."

    def has_permission(self, request, view):
        user = request.user

        if not user or not user.is_authenticated:
            return False

        if user.is_superuser:
            return True

        perfil = getattr(user, "perfil", None)

        return perfil is not None and perfil.tipo == "admin"
    