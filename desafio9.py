print('-' * 50)
conjunto1 = {"Ana", "Bruno", "Camila", 'João', "Diego", "Fernanda"}
conjunto2 = {"Gabriel", "Isabela", "João", "Larissa", "Marcelo"}
conjunto = conjunto1.union(conjunto2)
lista1 = list(conjunto1)
lista2 = list(conjunto2)
lista3 = list(conjunto)
print(f'A união dos dois conjuntos é {conjunto}')
print('-' * 50)
i = 0
while i < len(lista1):
    if lista1[i] in lista2:
        print(f'O Nome {lista1[i]} está nos dois conjuntos')
    i += 1
print('-' * 50)
i = 0
print('A Diferença entre os conjuntos é composta pelos nomes: ', end='')
while i < len((lista1)):
    if lista1[i] not in lista2:
        print(lista1[i], end=', ')
    i += 1
i = 0
while i < len((lista2)):
    if lista2[i] not in lista1:
        print(lista2[i], end=', ')
    i += 1
print('')
print('-' * 50)
