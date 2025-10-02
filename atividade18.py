salario = float(input('Digite o salário atual: R$'))
if salario <= 280:
    reajuste = 20
elif salario > 280 and salario <= 700:
    reajuste = 15
elif salario > 700 and salario <= 1500:
    reajuste = 10
else:
    reajuste = 5
reajuste_decimal = reajuste / 100
aumento = salario * reajuste_decimal
salario_reajustado = salario + (aumento)
print(f'''O salário antes do reajuste é igual a R${salario:.2f}
O percentual de Juros aplicado foi {reajuste}%
O salário aumentou em R${aumento:.2f}
O novo salário é igual a R${salario_reajustado:.2f}''')
