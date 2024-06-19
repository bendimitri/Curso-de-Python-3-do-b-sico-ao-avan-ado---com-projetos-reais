nome =  input("Digite seu nome:")

n_letra = len(nome)

contador = 0

while contador < n_letra:
    print(f"*{nome[contador]}*")
    contador += 1
print("Acabou...")



nome =  input("Digite seu nome:")


indice = 0
novo_nome = ""
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
print(novo_nome)
print("Acabou...")