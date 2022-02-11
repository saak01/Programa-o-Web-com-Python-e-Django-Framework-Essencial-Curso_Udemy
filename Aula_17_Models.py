"""
Models-

Como o proprio nome já diz, models é um modelo de dados/ 

Criando os modelos:
-Para criar o modelo é necessário criar uma classe, e está classe vai herdar da classe models.Model. Exemplo:

class Produto(models.Model):
    nome = models.CharField('Nome',max_length=100)
    preco = models.DecimalField('Preço')
    estoque = IntegerField('Quantidade em estoque')

Depois de adicionar o model, devemos fazer a migração para o banco de dados do seguinte modo:

python3 manage.py makemigrations 


"""
