from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("O email é obrigatório")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser precisa ter is_staff=True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser precisa ter is_superuser=True")

        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

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
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
