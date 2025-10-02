nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media == 10:
    print(f'Aprovado com distinção, sua nota é {media}')
elif media >= 7:
    print(f'Aprovado, sua nota é {media}')
elif media < 7:
    print(f'Reprovado, sua nota é {media}')
