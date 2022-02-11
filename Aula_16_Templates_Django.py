"""
Templates Django

Após todo o redirecionamento de templates para pasta  do app, lá podemos criar os arquivos html que foram citados nas rodas.
O conteudo deste arquivo carregam na página.

Podemos passar qualquer informação neste templates, estas informações são passadas nas funções em 'views':
OBS: Está dentro do diretório views do app.

def index(request):
   # context = {
        'curso':'Programação Web com Django Framework'
    }
    return render(request, 'index.html',contex

Para adicionarmos essa informação, colocamos a chave do dicionário, dentro de duas chaves, segue exemplo:

<h2>{{curso}}</h2>b

"""
