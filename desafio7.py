conjunto1 = {1.23, 8.67, 2.5, 9.99, 6.01}
conjunto2 = {3.14, 7.25, 0.99, 12.5, 4.75}
conjunto_final = conjunto1.union(conjunto2)
lista_conjuntos = list(conjunto_final)
i = soma = 0
while i < len(lista_conjuntos):
    soma += lista_conjuntos[i]
    i += 1
print(f'A soma de todos os valores listados em todos os conjuntos é igual a {soma}')
