"""
n1 = input("(E)ntra (S)sair:")

if n1 == "E":
    print("Entrando..")

else:
    print ("Saindo...")
"""




entrar = input("[E]ntrar [S]air:")
usuario = input("-----Cadastro----- \nUsuario: ")
senha = input("Senha:")

if entrar == "E" or "e":
    usuarioP = input("-----Login----- \nUsuario:")
    senhaP = input("Senha:")
    if senha == senhaP and usuario == usuarioP:
        print("Entrando!")
    else:
        print("Erro!")
else:
    print("Saindo!")

