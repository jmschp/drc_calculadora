from django.db import models
from django.utils import timezone

# Create your models here.


class Marca(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    data_criado = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):
    nome = models.CharField(max_length=255, unique=True)
    qtd_ml = models.PositiveIntegerField()
    concentracao_cbd_mg = models.PositiveIntegerField()
    garrafa = [("PPT", "Pipeta"), ("SPR", "Spray")]
    tipo_garrafa = models.CharField(
        max_length=3,
        choices=garrafa,
        default="PPT"
    )
    preco = models.FloatField()
    data_criado = models.DateTimeField(default=timezone.now)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
