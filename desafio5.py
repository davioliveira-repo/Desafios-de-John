despesas = {'aluguel', 'academia', 'alimentação'}
despesas.add('emergência')
despesas.add(str(input('Digite uma despesa para adicionar ao conjunto: ')))
lista_despesas = list(despesas)
i = 0
while i < len(lista_despesas):
    print(lista_despesas[i])
    i += 1
