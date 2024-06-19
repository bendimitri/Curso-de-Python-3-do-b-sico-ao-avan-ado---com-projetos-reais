string = "Casal Casal"

i = 0

while i < len(string):
    letra = string[i]

    if letra == " ":
        break
    print(letra)
    i += 1

else:
    print('Não achei espaço!')
print('Fora while')