"""
Usando django Shell
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
-Para saber de todos comandos shell do django é necessário usar : python3 manage.py

Podemos entrar no shell do django, muito parecido com o do python, para entrar é usar: python3 manage.py shell
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
comandos:

dir() -> para analisar a classe desejada:

from core.models import Produto
dir(Produto)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Podemos instanciar um objeto e salva-lo sem utilizar o admin, pelo django shell.:

from core.models import Produto
 produto1 =  Produto(nome='Atari 2000', preco = 199.76, estoque_restante = 155) #Como não existe um método construtor, temos que, adicionar cada nome.
 produto1.save()
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#E com o objeto instanciado podemos fazer tudo o que é feito no python shell.
Podemos alterar os objetos instanciados.

>>> p1 = Produto(nome="Xbox Series S", preco = 2999.90, estoque_restante=20)
>>> p1.save()
>>> p1.estoque_restante = 300
>>> p1.save()
---------------------------------------------------------------------------------------------------------------------------------------------------
Para apagar, usamos o comando:

p1 -> objeto instanciado:

p1.delete()
---------------------------------------------------------------------------------------------------------------------------------------------------
WiSG -> é o padrão python para  web.
---------------------------------------------------------------------------------------------------------------------------------------------------
Usando o dir, podemos achar ferramentas para usuabilidades desejadas, neste exemplo, usamos o request.header e consiguimos a informação do sistema operacional e 
navegador do usuario:

def index(request):
    context = {
        'curso':'Programação Web com Django Framework',
        'sistema_operacional':request.headers['User-Agent'] ###
       }
  
    return render(request, 'index.html',context)

Ápos a adição, chamamos pela chave, no arquivo index dentro da pasta templates como vimos anteriormente.
---------------------------------------------------------------------------------------------------------------------------------------------------



"""
