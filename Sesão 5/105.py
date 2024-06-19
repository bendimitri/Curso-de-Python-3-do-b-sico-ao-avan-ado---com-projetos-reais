"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""


""" def Print(a, b, c):
    print('casa1')
    print('casa2')
    print('casa3')
    print('casa4')
    print('casa5')
Print() """
def imprimir(nome="Sem nome"):
    print(f'Olá {nome}!')

imprimir('Dimitri Robert')
