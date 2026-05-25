from rest_framework import serializers
from .models import Servico, Agendamento
from datetime import timedelta

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = ["id", "nome", "valor", "duracao_minutos",]

class AgendamentoSerializer(serializers.ModelSerializer):
    servicos = serializers.PrimaryKeyRelatedField(queryset=Servico.objects.all(),many=True)
    hora_fim = serializers.SerializerMethodField()
    valor_total = serializers.SerializerMethodField()
    duracao_total_minutos = serializers.SerializerMethodField()

    class Meta:
        model = Agendamento
        fields = [
            "id", 
            "cliente", 
            "barbeiro", 
            "servicos", 
            "data_hora",
            "hora_fim",
            "valor_total",
            "duracao_total_minutos"
        ]
        read_only_fields = [
            "id",
            "cliente",
            "hora_fim",
            "valor_total",
            "duracao_total_minutos",
        ]


    def validate(self, attrs):
        barbeiro = attrs.get("barbeiro")
        servicos = attrs.get("servicos")
        data_hora = attrs.get("data_hora")

        cliente = None
        request = self.context.get("request")

        if request and request.user.is_authenticated:
            cliente = request.user.perfil

        if self.instance:
            barbeiro = barbeiro or self.instance.barbeiro
            data_hora = data_hora or self.instance.data_hora
            cliente = cliente or self.instance.cliente

            if servicos is None:
                servicos = list(self.instance.servicos.all())

        if not servicos:
            raise serializers.ValidationError({
                "servicos": "Selecione pelo menos um serviço."
            })

        if barbeiro.tipo != "barbeiro":
            raise serializers.ValidationError({
                "barbeiro": "O perfil selecionado precisa ser do tipo barbeiro."
            })

        if cliente and cliente.tipo != "cliente":
            raise serializers.ValidationError({
                "cliente": "Apenas perfis do tipo cliente podem criar agendamentos."
            })

        duracao_total = sum(
            servico.duracao_minutos
            for servico in servicos
        )

        novo_inicio = data_hora
        novo_fim = novo_inicio + timedelta(minutes=duracao_total)

        agendamentos_do_barbeiro = Agendamento.objects.filter(
            barbeiro=barbeiro,
            data_hora__lt=novo_fim
        ).prefetch_related("servicos")

        if self.instance:
            agendamentos_do_barbeiro = agendamentos_do_barbeiro.exclude(
                pk=self.instance.pk
            )

        for agendamento in agendamentos_do_barbeiro:
            inicio_existente = agendamento.data_hora
            fim_existente = agendamento.hora_fim

            if novo_inicio < fim_existente and novo_fim > inicio_existente:
                raise serializers.ValidationError({
                    "data_hora": "Este barbeiro já possui um agendamento nesse intervalo de horário."
                })

        if cliente:
            agendamentos_do_cliente = Agendamento.objects.filter(
                cliente=cliente,
                data_hora__lt=novo_fim
            ).prefetch_related("servicos")

            if self.instance:
                agendamentos_do_cliente = agendamentos_do_cliente.exclude(
                    pk=self.instance.pk
                )

            for agendamento in agendamentos_do_cliente:
                inicio_existente = agendamento.data_hora
                fim_existente = agendamento.hora_fim

                if novo_inicio < fim_existente and novo_fim > inicio_existente:
                    raise serializers.ValidationError({
                        "data_hora": "Você já possui um agendamento nesse intervalo de horário."
                    })

        return attrs

    def get_hora_fim(self, obj):
        return obj.hora_fim

    def get_valor_total(self, obj):
        return obj.valor_total

    def get_duracao_total_minutos(self, obj):
        return obj.duracao_total_minutos