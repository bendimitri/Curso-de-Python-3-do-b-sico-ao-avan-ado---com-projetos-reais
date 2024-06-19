n1 = input("Numero1:")
n2 = input("Numero2:")

expresao = input("Qual expresão você quer fazer \n(+)\n(-)\n(x):")

if expresao.startswith('+'):
    print (n1+n2)
elif expresao.startswith("x")
    print (n1*n2)
elif expresao.startswith("-")
    print (n1-n2)
else:
    print("Não entendi...")
print("Acabou!")