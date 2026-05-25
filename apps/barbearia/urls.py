from rest_framework.routers import DefaultRouter
from .views import ServicoViewSet, AgendamentoViewSet

router = DefaultRouter()

router.register(r'servicos', ServicoViewSet, basename='servico')
router.register(r"agendamentos", AgendamentoViewSet, basename="agendamento")

urlpatterns = router.urls
