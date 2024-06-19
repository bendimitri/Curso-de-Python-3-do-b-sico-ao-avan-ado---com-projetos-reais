entrar = input("[E]ntrar [S]air:")
usuario = input("-----Cadastro----- \n Usuario: ")
senha = input("Senha:")

if entrar == "E" or "e":
    usuarioP = input("Usuario:")
    senhaP = input("Senha:")
    if senha == senhaP and usuario == usuarioP:
        print("Entrando!")
    else:
        print("Erro!")
else:
    print("Saindo!")



"""


  """