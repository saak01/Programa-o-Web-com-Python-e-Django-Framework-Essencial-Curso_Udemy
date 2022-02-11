"""
Area administrativa do django
------------------------------------------------------------------------------------------------------------------------------------------------------------
-Por padrão o django vem com uma aplicação pré instalada de administração(admin), podemos checar isso pelo app instalados e urlspatter passada.

Para entrar nessa aplicação precisamos criar um super usuario com o comando: python3 manage.py creatsuperuser
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Podemos acessar os models que criamos nessa área de administração, para isso devemos ir no arquivo admin que se encontra no app e passar o seguinte comando:

from django.contrib import admin
from .models import Produto,Cliente 
# Register your models here.

admin.site.register(Produto)
admin.site.register(Cliente)

#Primeiramente importamos os models desejados, e dps passamos o codigo admin.site.register(MODELDESEJADO)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Quando adicionamos algum objeto, o nome que fica visivel não é o do objeto, mas isso é facil de resolver. É só irmos para o arquivo models e criar a seguinte função:

def __str__(self):
    return self.nome

#__str__ -> dunder self retorna o nome do objeto a página de admin.
-------------------------------------------------------------------------------------------------------------------------------------------------------------
Podemos fazer um classe no admin para conter todos os atributos da classe. Exemplo abaixo:

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','estoque_restante')


admin.site.register(Produto,ProdutoAdmin)

#Apos criada classe é necessário declara-la no admin.site.register()
-------------------------------------------------------------------------------------------------------------------------------------------------------------
OBS: é recomendado trocar a rota do admin para outra.

"""


