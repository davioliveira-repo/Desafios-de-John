while True:
    senha = str(input('Digite uma senha de no mínimo 8 caracteres: ')).strip()
    if len(senha) >= 8:
        break
    else:
        print('Senha Inválida!')
        continue
while True:
    senha2 = str(input('Confirme a senha: '))
    if senha == senha2:
        print('Senhas Confirmadas!')
        break
    else:
        print('Senhas Diferentes!')
        continue
print('Programa Finalizado!')
