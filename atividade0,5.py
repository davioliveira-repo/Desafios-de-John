num = int(input('Digite um número: '))
num += 2
print(num)


num = int(input('Digite um número qualquer: '))
if num % 2 == 0:
    print('O número é par')
else:
    print('O número é ímpar')

palavra = str(input('Digite a palavra: ')).strip()
print(f'A palavra apenas em letras maiúsculas é: {palavra.upper()}')
print(f'A palavra apenas em letras minúsculas é: {palavra.lower()}')
print(f'A palavra capitalizada é: {palavra.capitalize()}')
print(f'O número de caracteres que a palavra possui é: {len(palavra)}')

