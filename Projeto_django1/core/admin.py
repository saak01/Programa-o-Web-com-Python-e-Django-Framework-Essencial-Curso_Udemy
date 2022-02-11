from django.contrib import admin
from .models import Produto,Cliente 
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque_restante')
    
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')
    


admin.site.register(Produto,ProdutoAdmin)
admin.site.register(Cliente,ClienteAdmin)

