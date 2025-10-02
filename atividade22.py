from math import sqrt

a = float(input('Digite o valor de A: '))
if a == 0:
    print('Essa equação não é do segundo grau!')
else:
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
    delta = (b * b) - 4 * a * c
    if delta < 0:
        print(f'O Valor de Delta é {delta}, logo, não possui raízes reais!')
    elif delta == 0:
        raiz = (-b + sqrt(delta)) / (2 * a)
        print(f'Como Delta é igual a {delta}, possui duas raízes reais iguais, sendo elas iguais a {raiz}')
    else:
        raiz1 = (-b + sqrt(delta)) / (2 * a)
        raiz2 = (-b - sqrt(delta)) / (2 * a)
        print(f'A raízes da equação são iguais a {raiz1:.2f} e {raiz2:.2f}')
