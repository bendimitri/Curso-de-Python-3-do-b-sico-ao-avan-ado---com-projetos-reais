n1 = input('Digite um numero inteiro:')
n2 = n1.isdigit


if n2 == False:
    print('Tenque ser um numero inteiro!')

    
else:
    print('É um numero inteiro!')
    n3 = int(n1) % 2
    if n3 == 0:
        print('É um numero par!')
    else:
        print('É um numero impar!')

