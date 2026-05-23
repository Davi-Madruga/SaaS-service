from rest_framework import serializers
from .models import Perfil
from django.db import transaction
from django.contrib.auth import get_user_model
User = get_user_model()

class PerfilSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:

        model = Perfil
        fields = ["id","nome","telefone","tipo","email"]
        read_only_fields = ["id", "email", "tipo"]

class CadastroClienteSerializer(serializers.Serializer):
    nome = serializers.CharField()
    telefone = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)    

    def validate_email(self, value):
        email = value.strip().lower()

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Não foi possível realizar o cadastro")

        return email
    
    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )

        perfil = Perfil.objects.create(
            user = user,
            nome = validated_data['nome'],
            telefone = validated_data['telefone'],
            tipo = 'cliente'
        )
        
        return {
            'id': perfil.id,
            'nome': perfil.nome,
            'telefone': perfil.telefone,
            'tipo': perfil.tipo,
            'email': user.email
        }
