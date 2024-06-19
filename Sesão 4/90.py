compras = []
while True:
        n1 = input("\tSelecione uma opção:\n[I]Inserir    [A]Apagar    [L]Listar\n")
        compras_enumeradas = tuple(enumerate(compras))

        if n1 == "i" or n1 == "I":
            inserindo = input("Inserindo:")
            if inserindo == "":
                print('Ensira algo...')
                continue
            else:
                compras.append(inserindo)
            for compra_enumerada in enumerate(compras):
                for valor in compra_enumerada:
                    print(valor)
                continue



        elif n1 == "a" or n1 ==  "A":
            apagando = input("Apagando:")
            if apagando.isdigit():
                print("arroz")
                list(compras)
                apagando = int(apagando)
                del(compras)[apagando]
            else:
                print('Digite um numero...')
                continue



        elif n1 == "l" or n1 ==  "L":
            print(compras) 
            continue