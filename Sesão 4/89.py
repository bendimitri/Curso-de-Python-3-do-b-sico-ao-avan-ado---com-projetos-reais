lista = ["Anna","Gabriel","João"]

lista.append('Dimitri')

lista_enumerada = tuple(enumerate(lista, start=10))
#print(next(lista_enumerada))
print("---------------------------------")

print(lista_enumerada)
print("---------------------------------")

for tupla_enumerada in enumerate(lista):
    print('For da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')