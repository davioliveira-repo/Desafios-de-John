notas = [10, 5, 3]
i = 0
soma = 0
while i < len(notas):
    soma += notas[i]
    i += 1
media = soma / len(notas)
print(f'Sua média é {media:.1f}')
if media <= 5:
    print('Reprovado')
elif media >= 6:
    print('Aprovado')
