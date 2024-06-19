#cpf: 147 767 119 66
#cpf: 746 824 890 70
#--
#Ex.:  746.824.890-70 (746824890)
#  10  9  8  7  6  5  4  3  2
#  x   x  x  x  x  x  x  x  x
#  7   4  6  8  2  4  8  9  0
#  =   =  =  =  =  =  =  =  =
#  70  36 48 56 12 20 32 27 0
#--
#Somar todos os resultados: 
#70+36+48+56+12+20+32+27+0 =   301                          301
#Multiplicar o resultado anterior por 10
#301 * 10 =  3010                                          3010
#Obter o resto da divisão da conta anterior por 11
#3010 % 11 =  7                                             7

#Se o resultado anterior for maior que 9:
#    resultado é  0                                        0
#contrário disso:
#    resultado é o valor da conta
#O primeiro dígito do CPF é 7
#"""

cpf = "746.824.890-70"
cpf1 = "147.767.119-66"
    #  012345678910
    #iguinorar: 3-7-11
multiplicador = 10
contador = 0
comparasao = cpf[10]
listaconta = []
while True:
        for contadorCPF in cpf:
            if contador < 11 and multiplicador > 1:
                try:
                    int(contadorCPF)
                    multiCPF = int(contadorCPF) * multiplicador
                    listaconta.append(multiCPF)
                    multiplicador = multiplicador -1
                    contador += 1 
                except:
                    continue
                contador = 0 
                contador2 = 1
            else:
                soma = 0
                for i in range(8):
                    soma += listaconta[i]
                resto = soma * 10 % 11
                if resto > 9:
                    print("Numero 1 = 0")
                else:
                    print(f"Numero 1 = {resto}") 
        break                    

        



                


