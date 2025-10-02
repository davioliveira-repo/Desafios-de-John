from datetime import date

ano = int(input('Digite o seu ano de nascimento: '))
idade = (date.today().year) - ano

if idade == 18:
    print('Você deverá se alistar imediatamente!')
elif idade < 18:
    anos_novo = 18 - idade
    if anos_novo > 1:
        print(f'Você ainda é muito novo para se alistar! Faltam exatos {anos_novo} anos para seu alistamento!')
    else:
        print(f'Você ainda é muito novo para se alistar! Falta exato {anos_novo} ano para seu alistamento!')
else:
    print('Você já é muito velho para se alistar!')
