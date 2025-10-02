num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
palavra = str(input('Digite uma palavra qualquer: ')).strip()
if num1 > num2:
    print('O primeiro número é maior que o segundo')
print(f'{palavra * 3}')
print(f'{num1} x {num2} = {num1 * num2}')
