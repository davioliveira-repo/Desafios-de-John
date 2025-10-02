valor_hora = float(input('Digite o valor da sua hora de trabalho: R$'))
quantidade_hora = int(input('Digite a quantidade de horas que você trabalhou: '))
salario_bruto = valor_hora * quantidade_hora
desconto_FGTS = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.10
porcentagem_IR = 0
if salario_bruto <= 900:
    desconto_IR = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    porcentagem_IR = 5
    decimal_IR = 0.05
    desconto_IR = salario_bruto * decimal_IR
elif salario_bruto > 1500 and salario_bruto <= 2500:
    porcentagem_IR = 10
    decimal_IR = 0.10
    desconto_IR = salario_bruto * decimal_IR
elif salario_bruto > 2500:
    porcentagem_IR = 20
    decimal_IR = 0.20
    desconto_IR = salario_bruto * decimal_IR
print(f'''O salário bruto é: R${salario_bruto:.2f}
Desconto IR ({porcentagem_IR}%): R${desconto_IR:.2f}
Desconto INSS (10%): R${desconto_inss:.2f}
Desconto FGTS (11%): R${desconto_FGTS:.2f}
Salário Líquido: R${salario_bruto - (desconto_FGTS + desconto_IR + desconto_inss):.2f}''')
