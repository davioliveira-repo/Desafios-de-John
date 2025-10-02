sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
if sexo == 'M':
    print('O seu sexo é masculino!')
elif sexo == 'F':
    print('O seu sexo é feminino!')
else:
    print('Sexo inválido')
