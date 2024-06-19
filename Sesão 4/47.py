nome = input("Qual o seu nome:")
idade = input("Quantos anos você tem:")
n1 = len(nome)

if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome é alcontrario é {nome[-1:-30:-1]}")
    if " " in nome:
        print("Seu nome tem espaço!")
    else:
        print("Seu nome não tem espaço!")
    print(f"Seu nome contem {n1} letras!")
    print(f"A primeira letra do seu nome é {nome[0:1]}")
    print(f"A ultima letra do seu nome é {nome[-1-0]}")

else:
    print("Você deixou campos vazios!")



















"""

n1 =  input('Qual o seu nome:')
n2 =  input('Qual sua idade:')
n3 = len(n1)

if n1 and n2:
    print(f'Seu nome é:{n1} \nSeu nome Invertido é:{n1[-1:-100:-1]}')

    if " " in n1:
        print("Seu nome tem Espaço!")

    else:
        print("Seu nome não tem espaçõ!")
    
    print(f"Seu nome tem {n3} letras")
    print(f"A primeira letra do seu nome é {n1[0:1]}")
    print(f"A ultima letra do seu nome é {n1[-1:-2:-1]}")

else:
    print("Não entendi oque você falou!")

"""