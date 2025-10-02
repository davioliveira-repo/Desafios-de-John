while True:
    nome = str(input('Digite o nome da pessoa: ')).strip()
    idade = int(input('Digite a idade da pessoa: '))
    salario = float(input('Digite o salário da pessoa: R$'))
    sexo = str(input('Digite o sexo da pessoa: ')).strip().lower()[0]
    estado_civil = str(input('Digite o seu estado civil [S, C, V, D]: ')).strip().lower()[0]
    escolha = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if len(nome) > 3:
        print('O nome da pessoa tem mais que 3 caracteres!')
    elif len(nome) < 3:
        print('O nome da pessoa tem menos que 3 caracteres!')
    if idade >= 0 and idade <= 150:
        print('A idade da pessoa está entre 0 e 150')
    elif idade < 0 and idade > 150:
        print('A idade da pessoa não está entre 0 e 150')
    if salario > 0:
        print('O salário da pessoa é maior que 0')
    elif salario <= 0:
        print('O salário da pessoa é menor ou igual a 0')
    if sexo == 'f':
        print('O sexo da pessoa é feminino')
    elif sexo == 'm':
        print('O sexo da pessoa é masculino')
    if estado_civil == 'd':
        print('A pessoa é divorciada')
    elif estado_civil == 's':
        print('A pessoa é solteira')
    elif estado_civil == 'v':
        print('A pessoa é viúva')
    elif estado_civil == 'c':
        print('A pessoa é casada')
    if escolha == 'N':
        break
print('Obrigado por utilizar o nosso programa!')