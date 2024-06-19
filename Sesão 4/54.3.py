n1 = input("Qual seu nome?")
n2 = len(n1)
try:
     
    if n2 <= 4:
        print("Seu nome é muito curto!")
    elif n2 >= 5 and n2 <=6:
        print("Seu nome é normal!")
    elif n2 > 6:
        print("Seu nome é grande!")
    else:
        print("Não entendi!")
 
except:
    print("Seila!")