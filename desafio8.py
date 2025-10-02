estoque = [('produto1', 5, 10), ('produto2', 2, 20)]
i = total = 0
while i < len(estoque):
    produto, quantidade, preco = estoque[i]
    total += preco * quantidade
    print(total)
    i += 1