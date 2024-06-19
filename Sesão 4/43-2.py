n1 = input('Qual o seu nome:')

n2 = input('Oque quer encontra em nome?')

if n2 in n1:
    print(f'{n2} contem dentro de ({n1})')
else:
    print(f'({n2})não contem em ({n1})')


###############

nome = 'dimitri'
#0 1 2 3 4 5 6
#-4 -3 -2 -1
print(nome[3])
print(nome[-4])

print('z' not in nome) 
print('z' in nome) 



