letra = str(input('Digite uma letra qualquer: ')).strip().upper()
if letra in 'AEIOU':
    print('A letra é uma vogal!')
elif len(letra) > 1:
    print('Digite apenas uma letra!')
else:
    print('A letra é uma consoante!')