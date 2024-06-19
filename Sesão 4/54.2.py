n1 = int(input("Que horas são?"))

try:

    if n1 <= 11 and n1 >= 0:
        print("Bom dia!")
    elif n1 >= 12 and n1 <= 17:
        print("Boa tarde!")
    elif n1 >= 18 and n1 <= 23:
        print("Boa noite!")
    else:
        print("Não conheso essa hora!")
except:
    print("Isso não é um horario!")