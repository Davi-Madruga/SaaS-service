from rest_framework import serializers
from .models import Servico

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ["id", "nome", "valor", "duracao_minutos",]
