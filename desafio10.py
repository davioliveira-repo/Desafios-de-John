vendas = [('João', 'Notebook', 1500), ('Maria', 'Celular', 800), ('Cleiton', 'Tablet', 1200), ('João', 'Smart TV', 2200)]
total_vendas = {}
i = 0
while i < len(vendas):
    vendedor, produto, valor = vendas[i]
    if vendedor not in total_vendas:
        total_vendas[vendedor] = 0
    total_vendas[vendedor] += valor
    i += 1
    for vendedor, total in total_vendas.items():
        print(f'{vendedor} vendeu {total} no total')
