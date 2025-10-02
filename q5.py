# Desafio 5

lista1 = list()
lista2 = lista1[:]
soma1 = soma2 = 0
escolha = ''
while True:
    lista1.append(int(input('Digite um número para adicionar a lista 1: ')))
    escolha = str(input('Deseja encerrar a lista 1? [S/N]: ')).strip().lower()[0]
    if escolha == 's':
        break
while True:
    lista2.append(int(input('Digite um número para adicionar a lista 2: ')))
    escolha = str(input('Deseja encerrar a lista 2? [S/N]: ')).strip().lower()[0]
    if escolha == 's':
        break
for num in lista1:
    soma1 += num
for num in lista2:
    soma2 += num
resultado = soma1 + soma2
print(f'O Resultado da soma da lista1 {lista1} e da lista2 {lista2} é igual a {resultado}')
