n1STR =  input("Digite um numero:")
n1FLOT = input("Digite outro numero:")


try:
    n2 = float(n1STR)
    n3 = float(n1FLOT)
    n4 = n2 + n3
    print(f"A soma de {n1STR} e {n1FLOT} = {n4}" )
except:
    print("Isso não é um numero!")


















"""
n1 = int(input("Que velocidade esta:")) 
n2 = 90 

n3 = 60
n4 = 100

if n1 <=n3:
    print('Passo!')
else:
    print('Não passo!')
"""