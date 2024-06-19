#interpolação
#S = string
#F = float
#D e I = inteiros
#x = tudo em minusculo
#X = TUDO EM MAIUSCULO
nome = 'Luiz'
preco = 1000.492942
#variavel = '%s, o preço é R$%f' % (nome, preco)
variavel = '%s, o preço é R$%.2f' % (nome, preco)
variavel2 = '%s, o preço é R$1000.49' % nome
#%s porque a interpolação ve s como string e f como float
print(variavel)
print(variavel2)