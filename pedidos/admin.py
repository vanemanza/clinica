from django.contrib import admin
from .models import *


class ProductosAdmin(admin.ModelAdmin):
    list_display=("nombre", "precio", "stock")
    #search_fields=("nombre", "categorias") me da error supongo q xq categorias es rel foreingkey
    search_fields = ("nombre",)
    list_filter = ("categorias",)

    

admin.site.register(Categoria)
admin.site.register(Producto, ProductosAdmin )
admin.site.register(Pedidos)
