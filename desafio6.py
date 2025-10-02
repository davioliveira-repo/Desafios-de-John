lista = ["Table", "Computer", "Bottle", "Chair", "Phone"]
pesquisa = str(input('Digite qual palavra deseja pesquisar: ')).strip()
if pesquisa in lista:
    print('Palavra encontrada!')
else:
    print('Palavra não encontrada')
