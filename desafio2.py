produtos = [('produto1', 25), ('produto2', 15)]
nome_produto = str(input('Digite o nome do produto que deseja adicionar: '))
quantidade = int(input('Digite a quantidade: '))
produtos.append((nome_produto, quantidade))
i = 0
while i < len(produtos):
    produto, quantidade = produtos[i]
    print(f'Temos {quantidade} unidades de {produto}')
    i += 1
