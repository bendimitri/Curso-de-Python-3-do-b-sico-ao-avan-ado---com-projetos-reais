n_linha = 5
n_colunas = 5

linha = 1
while linha <= n_linha:
    colunas = 1
    while colunas <= n_colunas:
        print(f'{linha=} {colunas=}')
        colunas +=1
    linha += 1


print("Acabo...")