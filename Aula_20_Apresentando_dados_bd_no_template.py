"""
OBS: O help é seu amigo, use sempre para poder esclarecer duvidas.
OBS: Sempre nomear as rotas, para evitar erros.


Apresentando dados do banco de dados no Template:
----------------------------------------------------------------------------------------------------------------------------------

Primeiramente entramos no django shell: python3 manage.py shell



Ápos isso, importamos o model desejado, acessamos o model.objectsobjects - são os objetos, desta forma podemos acesasr algumas 
informações do objeto.

exemplos:

Produto.objects.count() -> conta quantos objetos temos para a class Produto, estes objetos também estão no BD

Produto.objects.all() - mostra todos os produtos.

---------------------------------------------------------------------------------------------------------------------------------------------
Passando todos os produtos para  a views:

    Primeiramente foi criado a a variavel produto, a variavel vai receber: Produto.objects.all()
    e dentro do contexto criado em views, podemos adicionar está nova variavel. Exemplo:

Arquivo: views.py

def index(request):
    produtos = Produto.objects.all() -> variavel com dados atrelados as informações coletadas do objeto
    context = {
        'curso':'Programação Web com Django Framework',
        'sistema_operacional':request.headers['User-Agent'],
        'produtos':produtos -> criando o chave e valor para poder usar o template.
       }
  
    return render(request, 'index.html',context)

def contato(request):
    return render(request,'contato.html')

Após esstá adição ao views, temos que ir no index.html e fazer um loop for para podermos apresentar na página:

arquivo: templates/index.html

    {% for produto  in  produtos %}
        <p>{{produto}}</p> -> não pode esquecer de fazer a chamada deste modo, se não, a página não ira mostrar o conteudo desejado.{}[]
    {% endfor %}

#OBS Cuidado para não colocar o query set- ao inves do iterator selecionado.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
Linkando um link ao produto desejado:


primeiramente criarmos o href no objeto desejado:


    <h1>Inicio do Index_Projeto</h1>
    
    <table>
        <thead>
            <tr>
                <th>Produto</th>
                <th>Preço</th>
            </tr>
        </thead>
        <tbody>
            {% for produto  in  produtos %}
            <tr>
                <td><a href="{% url 'produto' produto.id %}">{{produto.nome}}</a></td>  #aqui está sendo criado o link, e vinculando com o nome da rota que foi criada. Neste caso rota 'produto', e o produto id é o parãmetro.
                <td>{{produto.preco}}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    
</body>

</html>

"""
