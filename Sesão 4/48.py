"""
n1 =  input('Dobrarei o numero que digitar:')

if n1.isdigit():
    n2 = float(n1)
    print (f"O dobro de {n1} é {n2* 2:.2f}")
else:
    print('Isso não é um numero!')
"""

n1 = input('Numero:')

try:
    ...
    n2 = float(n1)
    print(n2*n2)

    ...
except:
    print("Erro!")
