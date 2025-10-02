lista = []
while True:
    lista.append(str(input('Digite uma palavra para adicionar-la a lista: ')))
    escolha = str(input('Deseja continuar? [S/N]: ')).strip().lower()[0]
    if escolha == 'n':
        break
print(f'A primeira palavra digitada foi: {lista[0]}')
print(f'A última palavra digitada foi: {lista[-1]}')
