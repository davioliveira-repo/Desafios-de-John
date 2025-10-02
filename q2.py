nomes = list()
while True:
    nomes.append(str(input('Digite um nome para a lista: ')))
    escolha = str(input('Deseja Continuar? [S/N]: ')).strip().lower()[0]
    if escolha == 'n':
        break
print(nomes)
print(f'A lista possui {len(nomes)} nomes!')
