"""
for in com listas
"""


lista = ['Maria', 'Helena', 'Luiz']
contador = 0
for nome in lista:
    print(contador,nome)
    contador += 1

 


lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for indice in indices:
    print(indice,lista[indice], )
