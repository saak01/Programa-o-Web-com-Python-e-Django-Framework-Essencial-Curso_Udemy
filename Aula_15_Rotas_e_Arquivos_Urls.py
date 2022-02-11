"""
Rotas


O arquivo de rotas pertence ao projeto, mais especificamente ao arquivo urls dentro do projeto criado.
-Criação da rota:

Para a criação da rota, primeiramente devemos ter criado as views desejado, apṍs a criação fazemos o import das funções criadas e adicionamos elas a path.
Segue o exemplo abaixo:

from core.views import index,contato

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('/contato',contato)
]
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
Server erro 500 -> O servidor tentou processar algo e não conseguiu.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

É uma falha de segurança, a rota ser mostrada. Por isso, para o desenvolvimento deixamos o 'debug' ligado, mas após o desenvolvimento o certo é deixar FALSE.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Melhoramento de rotas

-Não é ideal que todas as suas rotas estejam na url do projeto.

Neste modo, importamos o include e fazemos ligação da urls com um arquivo urls.py criado dentro da pasta do aplicativo. Exemplo:

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls'))
]


"""
