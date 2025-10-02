lista = list()
soma = 0
while True:
    num = int(input('Digite um número para a lista: '))
    soma += num
    lista.append(num)
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if escolha == 'n':
        break
print(lista)
print(f'A soma de todos os números da lista é {soma}')
