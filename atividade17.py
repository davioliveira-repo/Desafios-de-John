turno = str(input('Digite o turno em que você estuda [M, V, N, I]: ')).strip().upper()[0]
if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Boa tarde')
elif turno == 'N':
    print('Boa noite')
elif turno == 'I':
    print('Bom dia e Boa tarde futuro CLT :(')
else:
    print('Valor inválido')
