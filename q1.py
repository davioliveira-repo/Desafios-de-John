lista = list()
while True:
    n = int(input('Digite um número para adicionar a lista: '))
    lista.append(n)
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if escolha == 'n':
        break
print(lista)
print(f'O maior número da lista é {max(lista)}')
