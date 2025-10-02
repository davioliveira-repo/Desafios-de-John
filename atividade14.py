num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
maior = 0
menor = 0
if num1 > num2 and num1 > num3:
    maior = num1
    print(f'O número {maior} é o maior')
elif num2 > num1 and num2 > num3:
    maior = num2
    print(f'O número {maior} é o maior')
elif num3 > num1 and num3 > num2:
    maior = num3
    print(f'O número {maior} é o maior')
if num1 < num2 and num1 < num3:
    menor = num1
    print(f'O número {num1} é o menor')
elif num2 < num1 and num2 < num3:
    menor = num2
    print(f'O número {num2} é o menor')
elif num3 < num1 and num3 < num2:
    menor = num3
    print(f'O número {num3} é o menor')
