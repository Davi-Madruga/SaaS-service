from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Perfil(models.Model):
    TIPOS = [
        ('admin','Admin'),
        ('barbeiro','Barbeiro'),
        ('cliente','Cliente')
    ]

    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    nome = models.CharField(max_length=120, verbose_name='Nome')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    tipo = models.CharField(max_length=20,default='cliente', choices=TIPOS, verbose_name='Tipo do Perfil')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
