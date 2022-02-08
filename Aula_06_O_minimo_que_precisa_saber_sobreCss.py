"""
Css é uma sigla de Cascading Style Sheets, ou folhas de estilo em Cascata e pe usado para aplicar estilos nas paginas html.

Desenvolvido pelo w3c em 1996 para formatar as páginas html, já que as tags html foram projetadas para realizar marcações de páginas

A relação entre html e css é bem forte. Como o Html é um linguagem de marcação (o alicerce de um site) 
e o Css é focado no estilo do site (toda  a estética de um site), eles andam juntos.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CSS não é tecnicamente um necessidade, mas provavelmente você não gostaria de olhar para um site que usa apenas html, pois isso parecia completamente abandonado.

A forma não recomendada é adicionada junto do arquivo Html:

<style>
    body {
        background: navy;
        color:white
    }
</style> 

A forma recomendada de se adicionar estilos CSS em uma pagina html é com um arquivo externo.

Está forma está no exemplo do arquivo Css e Html, o arquivo html faz um link para o arquivo css, deste modo, podendo usar o css em um arquivo externo. Exemplo:

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Geek University_Testes</title>  
<link rel="stylesheet" href="Aula_06_Css.css"> 
</head>
<body>
</body>
</html>
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Anatomia de um comando CSS:

Um comando básico de CSS é composto por seletor e declaração que contem propriedade e valor.

SELETOR{
    propriedade: valor;

}

O seletor seleciona quais elementos da página receberão a formatação da propriedade com o valor especificado. Vimos a pouco que o seletor
pode ser um tag html, uma classe ou um id.

São muitas as propriedades e valores possiveis para a formatação de um pagian. Podemos formatar praticamente qualquer coisa, lembrando que estamos falando
de estilos, que envolve escolher: tamanho/tipo/cores de fonte, de paginas, alinhamento, posicionamento de seçoes e etc. 
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usamos Css para formatar página html de 3 formas diferentes:

1- Por elemento (tag) html: Usado quando queremos que todas as tagas especificadas recebem a mesmaa formatação:
exemplo:

body{
    background-color: red;
    color:white
}



2- Por classe usadao quando queremos que todos os elementos que incorporar a determinada classe receba a formatação.:

.verde {
    color:green;
    font-size: 42px;
}

3- Por id: Usado quando queremos que elementos individuais recebem a formatação:
OBS: id é unico, não é possivel repetir.


OBS: Todos os exemplos estão no arquivo "Aula_06_Css.css"
"""
