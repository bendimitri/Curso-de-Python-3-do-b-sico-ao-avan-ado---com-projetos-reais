#Operação ternário

#print('Valor' if True else 'Outro valor!')

#condição = 10 == 9
#variavel = 'Valor' if condição else 'Outro valor!'
#print(variavel)

digito = 9
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)