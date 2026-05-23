from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=80,verbose_name="Nome")
    valor = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.nome