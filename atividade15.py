produto1 = float(input('Digite o preço do primeiro produto: R$'))
produto2 = float(input('Digite o preço do segundo produto: R$'))
produto3 = float(input('Digite o preço do terceiro produto: R$'))
if produto1 < produto2 and produto1 < produto3:
    print(f'Você deve comprar o produto cujo preço é R${produto1:.2f}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'Você deve comprar o produto cujo preço é R${produto2:.2f}')
elif produto3 < produto1 and produto3 < produto2:
    print(f'Você deve comprar o produto cujo preço é R${produto3:.2f}')
