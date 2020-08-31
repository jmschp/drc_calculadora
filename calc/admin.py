from django.contrib import admin
from .models import Marca, Produto

# Register your models here.


class MarcaAdmin(admin.ModelAdmin):
    list_display = ("id", "data_criado", "nome")


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "marca", "nome", "qtd_ml", "concentracao_cbd_mg", "tipo_garrafa", "preco")
    exclude = ("data_criado",)


admin.site.register(Marca, MarcaAdmin)
admin.site.register(Produto, ProdutoAdmin)
