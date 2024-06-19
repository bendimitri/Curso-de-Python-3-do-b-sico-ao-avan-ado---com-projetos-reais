try:
    n1 =  int(input("Digite um numero inteiro!:"))
    print("Seu numero é inteiro!")
    n2 = n1%2
    if n2 == 0:
        print("E é par!")
    if n2 == 1:
        print("E é impar!")

except:
    print("Não é um inteiro!")


# ter ussado o (if n1.isdigit():)
    #Is digit
