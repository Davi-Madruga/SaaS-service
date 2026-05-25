from django.db import migrations
from django.contrib.auth.hashers import make_password


def criar_admin_inicial(apps, schema_editor):
    Usuario = apps.get_model("perfil", "Usuario")
    Perfil = apps.get_model("perfil", "Perfil")

    email = "admin@admin.com"
    senha = "admin123"

    usuario, created = Usuario.objects.get_or_create(
        email=email,
        defaults={
            "password": make_password(senha),
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
        }
    )

    if not created:
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.is_active = True
        usuario.save()

    Perfil.objects.get_or_create(
        user=usuario,
        defaults={
            "nome": "Administrador1",
            "telefone": "000000000",
            "tipo": "admin",
        }
    )


def remover_admin_inicial(apps, schema_editor):
    Usuario = apps.get_model("perfil", "Usuario")

    Usuario.objects.filter(email="admin@admin.com").delete()


class Migration(migrations.Migration):

    dependencies = [
        ("perfil", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(criar_admin_inicial, remover_admin_inicial),
    ]